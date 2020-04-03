-- SQL with Pokemon: Damage Multipliers
-- PostgreSQL 9.6
SELECT
  pokemon_name,
  str * multiplier AS modifiedStrength,
  element
FROM pokemon p
JOIN multipliers m ON p.element_id = m.id
WHERE
  str * multiplier >= 40
ORDER BY
  modifiedStrength DESC