-- Register for the Party (SQL for Beginners #3)
-- SQL - PostgreSQL 9.6
INSERT INTO participants(name, age, attending)
VALUES
  ('Javier', 42, TRUE);
SELECT
  *
FROM participants;