/* Easy SQL: LowerCase */
/* SQL - PostgreSQL 9.6 */
SELECT
  id,
  name,
  birthday,
  LOWER(race) as race
FROM demographics;