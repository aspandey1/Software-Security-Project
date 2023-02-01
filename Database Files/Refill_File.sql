DROP SCHEMA `medication_database`;
CREATE SCHEMA `medication_database` ;

CREATE TABLE `medication_database`.`patient_medication` (
  `PATIENT_ID` INT NOT NULL,
  `MEDICATION` VARCHAR(100) NOT NULL,
  `MEDICATION_INFO` VARCHAR(500) NOT NULL,
  `REFILL_STATUS` VARCHAR(50) NOT NULL);

INSERT INTO `medication_database`.`patient_medication` (`PATIENT_ID`, `MEDICATION`, `MEDICATION_INFO`, `REFILL_STATUS`) VALUES ('1', 'Atorvastatin', 'Atorvastatin is used to treat high cholesterol, and to lower the risk of stroke or heart attack.', 'NO');
INSERT INTO `medication_database`.`patient_medication` (`PATIENT_ID`, `MEDICATION`, `MEDICATION_INFO`, `REFILL_STATUS`) VALUES ('1', 'Levothyroxine', 'Levothyroxine treats hypothyroidism (low thyroid hormone). It is also used to treat or prevent goiter (enlarged thyroid gland).', 'NO');
INSERT INTO `medication_database`.`patient_medication` (`PATIENT_ID`, `MEDICATION`, `MEDICATION_INFO`, `REFILL_STATUS`) VALUES ('1', 'Lisinopril', 'Lisinopril is used to treat high blood pressure (hypertension) or congestive heart failure. It is also used to improve survival after a heart attack.', 'NO');
INSERT INTO `medication_database`.`patient_medication` (`PATIENT_ID`, `MEDICATION`, `MEDICATION_INFO`, `REFILL_STATUS`) VALUES ('1', 'Metformin', 'Metformin is used to improve blood sugar control in people with type 2 diabetes.', 'NO');
INSERT INTO `medication_database`.`patient_medication` (`PATIENT_ID`, `MEDICATION`, `MEDICATION_INFO`, `REFILL_STATUS`) VALUES ('1', 'Amlodipine', 'Amlodipine is used to treat high blood pressure. It is a calcium channel blocker, which relaxes blood vessels.', 'NO');
INSERT INTO `medication_database`.`patient_medication` (`PATIENT_ID`, `MEDICATION`, `MEDICATION_INFO`, `REFILL_STATUS`) VALUES ('2', 'Metoprolol', 'Metoprolol is a beta-blocker used to treat high blood pressure, chest pain, and heart failure.', 'NO');
INSERT INTO `medication_database`.`patient_medication` (`PATIENT_ID`, `MEDICATION`, `MEDICATION_INFO`, `REFILL_STATUS`) VALUES ('2', 'Albuterol', 'Albuterol is prescribed to treat asthma and breathing problems caused by chronic obstructive pulmonary disease (COPD). It is a medication known as a bronchodilator.', 'NO');
INSERT INTO `medication_database`.`patient_medication` (`PATIENT_ID`, `MEDICATION`, `MEDICATION_INFO`, `REFILL_STATUS`) VALUES ('2', 'Omeprazole', 'Omeprazole is prescribed to treat gastroesophageal reflux disease (GERD). It is also used to lower levels of acid in the stomach.', 'NO');
INSERT INTO `medication_database`.`patient_medication` (`PATIENT_ID`, `MEDICATION`, `MEDICATION_INFO`, `REFILL_STATUS`) VALUES ('2', 'Losartan', 'Losartan is used to treat high blood pressure (hypertension). It is also used to lower the risk of stroke in certain people with heart disease.', 'NO');
INSERT INTO `medication_database`.`patient_medication` (`PATIENT_ID`, `MEDICATION`, `MEDICATION_INFO`, `REFILL_STATUS`) VALUES ('3', 'Simvastatin', 'Simvastatin is used to lower cholesterol and triglycerides (types of fat) in the blood.', 'NO');
INSERT INTO `medication_database`.`patient_medication` (`PATIENT_ID`, `MEDICATION`, `MEDICATION_INFO`, `REFILL_STATUS`) VALUES ('4', 'Gabapentin', 'Gabapentin is an anticonvulsant used to treat epilepsy. It is also used to treat nerve pain.', 'NO');
INSERT INTO `medication_database`.`patient_medication` (`PATIENT_ID`, `MEDICATION`, `MEDICATION_INFO`, `REFILL_STATUS`) VALUES ('5', 'Hydrochlorothiazide', 'Hydrochlorothiazide is used to treat high blood pressure. It is a diuretic medication.', 'NO');
INSERT INTO `medication_database`.`patient_medication` (`PATIENT_ID`, `MEDICATION`, `MEDICATION_INFO`, `REFILL_STATUS`) VALUES ('5', 'Sertraline', 'Sertraline is used to treat depression, anxiety, panic attacks, post-traumatic stress disorder (PTSD), and obsessive-compulsive disorder (OCD).', 'NO');

