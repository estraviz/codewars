-- SQL with Sailor Moon: Thinking about JOINs...
-- PostgreSQL 9.6
SELECT
  sailorsenshi.senshi_name AS sailor_senshi,
  sailorsenshi.real_name_jpn AS real_name,
  cats.name AS cat,
  schools.school AS school
FROM sailorsenshi
LEFT JOIN cats ON sailorsenshi.cat_id = cats.id
LEFT JOIN schools ON sailorsenshi.school_id = schools.id