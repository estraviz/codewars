# SQL Basics: Simple table totaling

## Description

For this challenge you need to create a simple query to display each unique `clan` with their total points and ranked by their total points.

**`people table schema`**

* `name`
* `points`
* `clan`

You should then return a table that resembles below:

**`select on`**

* `rank`
* `clan`
* `total_points`
* `total_people`

The query must rank each clan by their `total_points`, you must return each unique clan and if there is no clan name you must replace it with `[no clan specified]`, you must sum the `total_points` for each clan and the `total_people` within that clan.
