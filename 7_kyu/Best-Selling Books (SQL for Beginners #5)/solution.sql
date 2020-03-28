-- Best-Selling Books (SQL for Beginners #5)
-- PostgreSQL 9.6
SELECT *
FROM books
ORDER BY copies_sold DESC
LIMIT 5