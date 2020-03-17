-- GROCERY STORE: Logistic Optimisation
-- PostgreSQL 9.6
SELECT
  COUNT(name) AS unique_products,
  producer
FROM products
GROUP BY
  producer
ORDER BY
  unique_products DESC,
  producer ASC