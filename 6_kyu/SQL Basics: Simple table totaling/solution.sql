-- SQL Basics: Simple table totaling
-- PostgreSQL 9.6
SELECT
  ROW_NUMBER () OVER (
    ORDER BY
      SUM(points) DESC
  ) AS rank,
  CASE
    WHEN clan = '' THEN '[no clan specified]'
    ELSE clan
  END AS clan,
  SUM(points) AS total_points,
  COUNT(name) AS total_people
FROM people
GROUP BY
  clan
ORDER BY
  total_points DESC