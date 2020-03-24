-- SQL: Padding Encryption
-- PostgreSQL 9.6
SELECT
  CONCAT(md5, REPEAT('1', LENGTH(sha256) - LENGTH(md5))) AS md5,
  CONCAT(REPEAT('0', LENGTH(sha256) - LENGTH(sha1)), sha1) AS sha1,
  sha256
FROM encryption