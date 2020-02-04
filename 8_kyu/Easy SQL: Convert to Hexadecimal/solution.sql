/* Easy SQL: Convert to Hexadecimal */
/*  SQL - PostgreSQL 9.6*/
select
  to_hex(legs) as legs,
  to_hex(arms) as arms
from monsters;