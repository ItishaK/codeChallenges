-- Create table PatientDetails Raw table
CREATE TABLE patientDetails_rw (
    patientID VARCHAR(10) PRIMARY KEY,
    age VARCHAR(10),
    gender VARCHAR(10),
    bmi VARCHAR(10),
    glucoseLevel VARCHAR(10),
    outcome VARCHAR(10),
    readmission VARCHAR(10),
    visitDate VARCHAR(10)
);

-- Data Import Statement from CSV File
COPY patientDetails_rw(patientID, age, gender, bmi, glucoseLevel, outcome, readmission, visitDate)
FROM 'input_path\diabetes_data.csv'
delimiter ','
csv header ;

-- Create table PatientDetails History table
create table patientDetails_history
    as select * from patientDetails_rw;

-- # Cross-Checking Data Imports
select * from patientDetails_rw limit 5;
select * from patientDetails_history limit 5;

select count(*) from patientDetails_rw;
select count(*) from patientDetails_history;

-- Data Quality Checks
-- 1. Check for Overall Row Count
select count(*) from patientDetails_rw as TotalRows;

-- 2. Check for NULL values
SELECT
    COUNT(*) AS TotalRecords,
    COUNT(*) - COUNT(PatientID) AS Null_PatientID,
    COUNT(*) - COUNT(Age) AS Null_Age,
    COUNT(*) - COUNT(Gender) AS Null_Gender,
    COUNT(*) - COUNT(BMI) AS Null_BMI,
    COUNT(*) - COUNT(GlucoseLevel) AS Null_GlucoseLevel,
    COUNT(*) - COUNT(Outcome) AS Null_Outcome,
    COUNT(*) - COUNT(Readmission) AS Null_Readmission,
    COUNT(*) - COUNT(VisitDate) AS Null_VisitDate
FROM patientDetails_rw;

-- - 3. Identify NULL values
SELECT *
FROM patientDetails_rw
WHERE visitDate IS NULL or gender IS NULL;

-- 4. Check for duplicate PatientID values
SELECT patientID, COUNT(*)
FROM patientDetails_rw
GROUP BY patientID
HAVING COUNT(*) > 1;

-- Check for distinct Boolean values i.e. outcome and readmission
Select distinct(outcome)
from patientDetails_rw;

Select distinct(readmission)
from patientDetails_rw;

-- Date Format validation Function
create function check_date(s varchar) returns boolean
language plpgsql
as $$
begin
  perform s::date;
  return true;
exception when others then
  return false;
end;
$$;

SELECT *,
       check_date(visitDate)
FROM patientDetails_rw
where check_date(visitDate) = False;

