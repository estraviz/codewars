-- Easy SQL: Counting and Grouping
-- PostgreSQL 9.6
SELECT
  race,
  COUNT(*) AS count
FROM demographics
GROUP BY
  race
ORDER BY
  count DESC;