-- SQL Basics - Trimming the Field
-- PostgreSQL 9.6
SELECT
  id,
  name,
  SPLIT_PART(characteristics, ',', 1) AS characteristic
FROM monsters
ORDER BY id