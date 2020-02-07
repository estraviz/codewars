/* On the Canadian Border (SQL for Beginners #2) */
/* SQL - PostgreSQL 9.6 */
SELECT
  name,
  country
FROM travelers
WHERE
  country NOT IN ('Canada', 'Mexico', 'USA');