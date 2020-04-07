-- SQL Basics: Maths with String Manipulations
-- PostgreSQL 9.6
SELECT
  (BIT_LENGTH(name) + LENGTH(race)) AS calculation
FROM demographics