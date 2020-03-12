-- SQL Basics: Simple JOIN
-- SQLite 3.2.8
SELECT
  p.*,
  c.name AS company_name
FROM products p
JOIN companies c ON p.company_id = c.id