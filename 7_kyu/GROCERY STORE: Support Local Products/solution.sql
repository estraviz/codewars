-- GROCERY STORE: Support Local Products
-- PostgreSQL 9.6
SELECT
  COUNT(*) AS products,
  country
FROM products
WHERE
  country IN ('United States of America', 'Canada')
GROUP BY
  country
ORDER BY
  products DESC