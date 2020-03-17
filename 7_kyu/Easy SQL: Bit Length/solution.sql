-- Easy SQL: Bit Length
-- PostgreSQL 9.6
select
  id,
  BIT_LENGTH(name) AS name,
  birthday,
  BIT_LENGTH(race) AS race
FROM demographics