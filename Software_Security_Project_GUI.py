#Ashish Pandey Software Security Project

from tkinter import *
from tkinter import messagebox
import mysql.connector
import datetime

# There are 5 patients in the database and thier IDs are 1,2,3,4,5. By changing the PATIENT_ID variable you can change the patient selected
PATIENT_ID = 1

# Need to change mySQL connection so it can work on other systems
global mycursorAskQuestion
askQuestionDB = mysql.connector.connect(host = "localhost", user="root", password="Kapilvastu1", database ="ask_question_database")
mycursorAskQuestion = askQuestionDB.cursor()

global mycursorSeeResult
seeResultDB = mysql.connector.connect(host = "localhost", user="root", password="Kapilvastu1", database ="result_database")
mycursorSeeResult = seeResultDB.cursor()

global mycursorMed
requestMedDB = mysql.connector.connect(host = "localhost", user="root", password="Kapilvastu1", database ="medication_database")
mycursorMed = requestMedDB.cursor()

global mycursorPayment
paymentDB = mysql.connector.connect(host = "localhost", user="root", password="Kapilvastu1", database ="payment_database")
mycursorPayment = paymentDB.cursor()

root = Tk()
root.geometry("500x500")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.title("SHIS")

def showFrame(frame):
    frame.tkraise()

def saveQuestion():
    input = question.get("1.0", "end-1c")
    query = ("UPDATE patient SET question = '%s' WHERE PATIENT_ID = %d;" %(input, PATIENT_ID))
    mycursorAskQuestion.execute(query)
    askQuestionDB.commit()
    showFrame(menuFrame)

def result():
    for widget in resultFrame.winfo_children():
        widget.destroy()
    
    res = []
    dateQuery = "SELECT RESULT FROM test_result WHERE DATE = %s;"
    mycursorSeeResult.execute(dateQuery, [(defaultValueDate.get())])
    res = mycursorSeeResult.fetchone()
    
    resultLabel = Label(resultFrame, text="Result:")
    patientResultLabel = Label(resultFrame, text=res[0])
    closeButton = Button(resultFrame, text="Close", command=lambda:showFrame(menuFrame))
    resultLabel.pack()
    patientResultLabel.pack()
    closeButton.pack()
    showFrame(resultFrame)

def showMedInfo(event):
    res = []
    medInfoQuery = ("SELECT MEDICATION_INFO FROM patient_medication WHERE MEDICATION = '%s' AND PATIENT_ID = %d;" %(defaultValueMed.get(), PATIENT_ID))
    mycursorMed.execute(medInfoQuery)
    res = mycursorMed.fetchone()
    medInfoLabel.configure(text=res[0])

def changeRefillStatus():
    refillStatusChangeQuery = ("UPDATE patient_medication SET REFILL_STATUS = 'YES' WHERE PATIENT_ID = %d AND MEDICATION = '%s';" %(PATIENT_ID, defaultValueMed.get()))
    mycursorMed.execute(refillStatusChangeQuery)
    requestMedDB.commit()
    showFrame(menuFrame)

# Process Payment using payment_database
def paymentProcess():
    total = []
    totalQuery = ("SELECT AMOUNT_DUE FROM patient_bills WHERE PATIENT_ID = %d" %PATIENT_ID)
    mycursorPayment.execute(totalQuery)
    total = mycursorPayment.fetchone()

    funds = []
    fundsQuery = ("SELECT CURRENT_FUNDS FROM patient_bills WHERE PATIENT_ID = %d" %PATIENT_ID)
    mycursorPayment.execute(fundsQuery)
    funds = mycursorPayment.fetchone()

    creditCardNum = []
    ccNoQuery = ("SELECT CREDITCARD_NUM FROM patient_bills WHERE PATIENT_ID = %d" %PATIENT_ID)
    mycursorPayment.execute(ccNoQuery)
    creditCardNum = mycursorPayment.fetchone()
    if (total[0] == 0.0):
        messagebox.showinfo(title="No Payment Due", message="Account Balance Has Been Paid")
        return

    
    if (cardEntry.get() == creditCardNum[0]):
        if(funds[0] - total[0] >= 0):
            newFunds = funds[0] - total[0]
            messagebox.showinfo(title="Sucessful", message="Payment Processed\nConfirmation Number: 312-629")
            updateAmountDue = ("UPDATE patient_bills SET AMOUNT_DUE = '0.00' WHERE PATIENT_ID = %d" %PATIENT_ID)
            mycursorPayment.execute(updateAmountDue)
            paymentDB.commit()
            updateCurrentFunds = ("UPDATE patient_bills SET CURRENT_FUNDS = '%f' WHERE PATIENT_ID = %d" %(newFunds, PATIENT_ID))
            mycursorPayment.execute(updateCurrentFunds)
            paymentDB.commit()
            billTotalLabel.configure(text="Bill Total: $0.00")
            showFrame(menuFrame)
        else:
            messagebox.showerror(title="Insufficient Funds", message="Bank Denied Payment")
    else:
        messagebox.showerror(title="Not Valid", message="The Credit Card Number Is Incorrect")

###--------------------------------------Menu Frame------------------------------------------------------###

menuFrame = Frame(root)
askQuestionButton = Button(menuFrame, text="Ask Question", command=lambda:showFrame(selectEmpFrame))
testResultButton = Button(menuFrame, text="Test Results", command=lambda:showFrame(selectResultFrame))
payBillButton = Button(menuFrame, text="Pay Bill", command=lambda:showFrame(payBillFrame))
requestRefillButton = Button(menuFrame, text="Request Refill", command=lambda:showFrame(medicationDisplayFrame))
askQuestionButton.pack()
testResultButton.pack()
requestRefillButton.pack()
payBillButton.pack()

###--------------------------------------Select Emp Frame---------------------------------------------------###

selectEmpFrame = Frame(root)
selectEmpLabel = Label(selectEmpFrame, text="Select Employee")

defaultValue = StringVar(selectEmpFrame)
defaultValue.set("Dr.Brad Smith") # default value

menu = OptionMenu(selectEmpFrame, defaultValue, "Dr.Brad Smith", "Dr.Alan Thomas", "Rick Lopez", "Selena Lee")

nextButton = Button(selectEmpFrame, text="Next", command=lambda:showFrame(askQuestionFrame))
selectEmpLabel.pack()
menu.pack()
nextButton.pack()

###--------------------------------------Ask Question Frame--------------------------------------------------###

askQuestionFrame = Frame(root)
questionLabel = Label(askQuestionFrame, text="Question")
question = Text(askQuestionFrame, height=20, width=50)
questionSubmitButton = Button(askQuestionFrame, text="Submit", command=saveQuestion)

questionLabel.pack()
question.pack()
questionSubmitButton.pack()

###--------------------------------------Select Result Frame------------------------------------------------------###

queryResults = []
dates = []
dateQuery = ("SELECT DATE FROM test_result WHERE PATIENT_ID = %d;" %PATIENT_ID)
mycursorSeeResult.execute(dateQuery)

for x in mycursorSeeResult:
    queryResults += x
for y in queryResults:
    dates.append(y.strftime('%Y-%m-%d %H:%M:%S'))

selectResultFrame = Frame(root)
selectResultLabel = Label(selectResultFrame, text="Select Date")

defaultValueDate = StringVar(selectResultFrame)
defaultValueDate.set(dates[0]) # default value
resultMenu = OptionMenu(selectResultFrame, defaultValueDate, *dates)
dateSubmitButton = Button(selectResultFrame, text="Submit", command=result)

selectResultLabel.pack()
resultMenu.pack()
dateSubmitButton.pack()

###---------------------------------------------See Test Result Frame------------------------------------------###

resultFrame = Frame(root)

###-------------------------------------------Refill Frame------------------------------------------------------###

queryResultsMed = []
medQuery = ("SELECT MEDICATION FROM patient_medication WHERE PATIENT_ID = %d;" %PATIENT_ID)
mycursorMed.execute(medQuery)

for x in mycursorMed:
    queryResultsMed += x

medicationDisplayFrame = Frame(root)
medicationLabel = Label(medicationDisplayFrame, text="Select Medication")

defaultValueMed = StringVar(medicationDisplayFrame)
defaultValueMed.set("Select Refill") # default value
medResultMenu = OptionMenu(medicationDisplayFrame, defaultValueMed, *queryResultsMed, command=showMedInfo)
medInfoLabel = Label(medicationDisplayFrame, text="", wraplength=400)
refillSubmitButton = Button(medicationDisplayFrame, text="Submit", command=changeRefillStatus)

medicationLabel.pack()
medResultMenu.pack()
medInfoLabel.pack()
refillSubmitButton.pack()

###--------------------------------------Pay Bill Frame------------------------------------------------------###

billTotal = []
billQuery = ("SELECT AMOUNT_DUE FROM patient_bills WHERE PATIENT_ID = %d" %PATIENT_ID)
mycursorPayment.execute(billQuery)
billTotal = mycursorPayment.fetchall()

payBillFrame = Frame(root)
billTotalLabel = Label(payBillFrame, text="Bill Total: $%.2f" %billTotal[0])
billTotalLabel.place(x=195, y=20)
creditCardLabel = Label(payBillFrame, text="Credit Card No:").place(x=150, y=50)
cardEntry = Entry(payBillFrame)
cardEntry.place(x=240,y=50)
format = Label(payBillFrame, text="Format: xxxx-xxxx-xxxx-xxxx", font=("Arial", 7)).place(x=235, y=70)
paymentSubmitButton = Button(payBillFrame, text="Submit", command=paymentProcess).place(x=190, y=100)
cancelPaymentButton = Button(payBillFrame, text="Cancel", command=lambda:showFrame(menuFrame)).place(x=260,y=100)

for frames in (menuFrame, selectEmpFrame, askQuestionFrame, selectResultFrame, resultFrame, medicationDisplayFrame, payBillFrame):
    frames.grid(row=0, column=0, sticky="nsew")

showFrame(menuFrame)

root.mainloop()