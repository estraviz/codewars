-- GROCERY STORE: Inventory
-- PostgreSQL 9.6
SELECT
  id,
  name,
  stock
FROM products
WHERE
  producent = 'CompanyA'
  AND stock <= 2
ORDER BY
  id