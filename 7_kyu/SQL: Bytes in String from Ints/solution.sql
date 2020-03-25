-- SQL: Bytes in String from Ints
-- PostgreSQL 9.6
SELECT
  LENGTH(CAST(number1 AS varchar)) AS octnum1,
  LENGTH(CAST(number2 AS varchar)) AS octnum2,
  LENGTH(CAST(number3 AS varchar)) AS octnum3,
  LENGTH(CAST(number4 AS varchar)) AS octnum4,
  LENGTH(CAST(number5 AS varchar)) AS octnum5
FROM numbers