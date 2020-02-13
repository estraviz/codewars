-- Collect Tuition (SQL for Beginners #4)
-- PostgreSQL 9.6
SELECT
  *
FROM students
WHERE
  tuition_received = FALSE;