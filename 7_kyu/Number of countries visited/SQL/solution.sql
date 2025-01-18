-- select each person and the number of countries they have visited
SELECT p.name as name, COUNT(DISTINCT(country_id)) AS countries_visited
FROM visits v
RIGHT JOIN people p
  ON p.id = v.person_id
GROUP BY name
ORDER by countries_visited DESC, name ASC
