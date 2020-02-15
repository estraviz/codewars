-- BASICS: Length based SELECT with LIKE
-- PostgreSQL 9.6
SELECT
  first_name,
  last_name
FROM names
WHERE
  first_name LIKE '______%';