-- Easy SQL: ASCII Converter
-- PostgreSQL 9.6
SELECT
  id,
  ASCII(LEFT(name, 1)) AS name,
  birthday,
  ASCII(LEFT(race, 1)) AS race
FROM demographics