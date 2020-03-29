# SQL with LOTR: Elven Wildcards

## Description

Deep within the fair realm of [Lothlórien](https://en.wikipedia.org/wiki/Lothl%C3%B3rien), you have been asked to create a shortlist of candidates for a recently vacated position on the council.

Of so many worthy [elves](https://en.wikipedia.org/wiki/Elf_(Middle-earth)), who to choose for such a lofty position? After much thought you decide to select candidates by name, which are often closely aligned to an elf's skill and temperament.

Choose those with _tegil_ appearing anywhere in their **first name**, as they are likely to be good calligraphers, **OR** those with _astar_ anywhere in their **last name**, who will be faithful to the role.

**`Elves table`**

* `firstname`
* `lastname`

_all names are in lowercase_.

To aid the scribes, return the `firstname` and `lastname` column concatenated, separated by a space, into a single `shortlist` column, and capitalise the first letter of each name.
