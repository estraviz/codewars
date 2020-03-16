-- GROCERY STORE: Real Price!
-- PostgreSQL 9.6
SELECT
  name,
  weight,
  price,
  weight,
  CAST(
    ROUND(CAST(price /(weight / 1000) AS NUMERIC), 2) AS DOUBLE PRECISION
  ) AS price_per_kg
FROM products
ORDER BY
  price_per_kg ASC,
  name ASC