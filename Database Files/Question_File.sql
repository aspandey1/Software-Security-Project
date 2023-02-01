DROP SCHEMA `ask_question_database`;
CREATE SCHEMA `ask_question_database` ;

CREATE TABLE `ask_question_database`.`patient` (
  `PATIENT_ID` INT NOT NULL,
  `PATIENT_NAME` VARCHAR(45) NOT NULL,
  `Question` VARCHAR(200),
  PRIMARY KEY (`PATIENT_ID`));

INSERT INTO `ask_question_database`.`patient` (`PATIENT_ID`, `PATIENT_NAME`) VALUES ('1', 'Brad Smith');
INSERT INTO `ask_question_database`.`patient` (`PATIENT_ID`, `PATIENT_NAME`) VALUES ('2', 'Tony Lopez');
INSERT INTO `ask_question_database`.`patient` (`PATIENT_ID`, `PATIENT_NAME`) VALUES ('3', 'Bill Rush');
INSERT INTO `ask_question_database`.`patient` (`PATIENT_ID`, `PATIENT_NAME`) VALUES ('4', 'Andy Lee');
INSERT INTO `ask_question_database`.`patient` (`PATIENT_ID`, `PATIENT_NAME`) VALUES ('5', 'Jim Parson');