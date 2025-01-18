# Number of countries visited

## How many foreign countries has each person visited?

### Description

In this kata, you are provided with a database that contains information about people and their visits to various countries.

Your task is to figure out how many countries each person has visited.

### Database Schema

**`people`** table:

- `id` (integer, primary key): Unique identifier for the person.
- `name` (string): The person's name. You can assume that the names are unique.

**`countries`** table:

- `id` (integer, primary key): Unique identifier for the country.
- `name` (string, unique): The name of the country.

**`visits`** table:

- `id` (integer, primary key): Unique identifier for the visit.
- `person_id` (integer, foreign key): Refers to a person.
- `country_id` (integer, foreign key): Refers to a country.
- `year` (integer): The year of the visit.

### Requirements

Return a list of people and the number of countries they have visited.

First, sort the list by the number of countries visited, from highest to lowest. Then, if any people have the same number of countries visited, sort them by the person's name ascending.

Include all people in the list, even if they haven't visited any foreign countries.

Make sure to count the number of different countries each person has visited, as opposed to their total number of visits.

### Example

Given this sample data:

**`people`**:

| id  | name  |
| --- | ----- |
| 1   | Tim   |
| 2   | Bob   |
| 3   | Sally |
| 4   | Alex  |

**`countries`**:

| id  | name          |
| --- | ------------- |
| 1   | Great Britain |
| 2   | Spain         |
| 3   | Argentina     |
| 4   | Montenegro    |
| 5   | Japan         |

**`visits`**:

| id  | person_id | country_id | year |
| --- | --------- | ---------- | ---- |
| 1   | 1         | 1          | 2019 |
| 2   | 1         | 4          | 2024 |
| 3   | 2         | 1          | 2000 |
| 4   | 2         | 2          | 2010 |
| 5   | 2         | 4          | 2012 |
| 6   | 2         | 4          | 2022 |
| 7   | 2         | 5          | 2023 |
| 8   | 3         | 4          | 2021 |

You should return the following result:

| name  | countries_visited |
| ----- | ----------------- |
| Bob   | 4                 |
| Tim   | 2                 |
| Sally | 1                 |
| Alex  | 0                 |
