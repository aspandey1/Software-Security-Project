DROP SCHEMA `result_database`;
CREATE SCHEMA `result_database` ;

CREATE TABLE `result_database`.`test_result` (
  `PATIENT_ID` INT NOT NULL,
  `DATE` DATETIME NOT NULL,
  `RESULT` VARCHAR(45) NOT NULL);
  
INSERT INTO `result_database`.`test_result` (`PATIENT_ID`, `DATE`, `RESULT`) VALUES ('1', '2022-01-11 10:30:00', 'Strep');
INSERT INTO `result_database`.`test_result` (`PATIENT_ID`, `DATE`, `RESULT`) VALUES ('1', '2022-02-10 11:30:00', 'Covid');
INSERT INTO `result_database`.`test_result` (`PATIENT_ID`, `DATE`, `RESULT`) VALUES ('1', '2022-03-07 12:30:00', 'Flu');
INSERT INTO `result_database`.`test_result` (`PATIENT_ID`, `DATE`, `RESULT`) VALUES ('1', '2022-04-03 14:30:00', 'Common Cold');
INSERT INTO `result_database`.`test_result` (`PATIENT_ID`, `DATE`, `RESULT`) VALUES ('1', '2022-05-25 16:30:00', 'Broken Finger');
INSERT INTO `result_database`.`test_result` (`PATIENT_ID`, `DATE`, `RESULT`) VALUES ('2', '2022-06-21 17:30:00', 'Burn');
INSERT INTO `result_database`.`test_result` (`PATIENT_ID`, `DATE`, `RESULT`) VALUES ('2', '2022-07-01 21:30:00', 'Flu Shot');
INSERT INTO `result_database`.`test_result` (`PATIENT_ID`, `DATE`, `RESULT`) VALUES ('3', '2022-08-22 22:30:00', 'Common Cold');
INSERT INTO `result_database`.`test_result` (`PATIENT_ID`, `DATE`, `RESULT`) VALUES ('4', '2022-09-21 23:30:00', 'Covid');
INSERT INTO `result_database`.`test_result` (`PATIENT_ID`, `DATE`, `RESULT`) VALUES ('4', '2022-10-19 09:30:00', 'Strep');
INSERT INTO `result_database`.`test_result` (`PATIENT_ID`, `DATE`, `RESULT`) VALUES ('5', '2022-11-13 08:30:00', 'Broken Foot');


