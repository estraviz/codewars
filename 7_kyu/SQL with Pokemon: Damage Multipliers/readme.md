# SQL with Pokemon: Damage Multipliers

## Description

You have arrived at the [Celadon Gym](https://pokemon.fandom.com/wiki/Celadon_City_Gym) to battle [Erika](https://pokemon.fandom.com/wiki/Erika) for the [Rainbow Badge](https://pokemon.fandom.com/wiki/Gym_Badges#Rainbow_Badge).

She will be using [Grass-type Pokemon](https://pokemon.fandom.com/wiki/Grass_type). Any fire pokemon you have will be strong against grass, but your water types will be weakened. The multipliers table within your [Pokédex](https://en.wikipedia.org/wiki/Gameplay_of_Pok%C3%A9mon#Pok%C3%A9dex) will take care of that.

Using the following tables, return the `pokemon_name`, `modifiedStrength` and `element` of the [Pokemon](https://en.wikipedia.org/wiki/Pok%C3%A9mon) whose strength, after taking these changes into account, is greater than or equal to 40, ordered from strongest to weakest.

**`pokemon schema`**

* `id`
* `pokemon_name`
* `element_id`
* `str`

**`multipliers schema`**

* `id`
* `element`
* `multiplier`
