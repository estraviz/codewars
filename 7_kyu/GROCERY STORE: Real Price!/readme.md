# GROCERY STORE: Real Price

## Description

You are the owner of the Grocery Store. All your products are in the database, that you have created after CodeWars SQL exercises! :)

Customer often need to now how much really they pay for the products. Manufacturers make different sizes of same product so it is hard to compare prices, sometimes they make packages look big, but the weight of the product is small.

Make a `SELECT` query which will tell the price per kg of the product.

Weight is in grams! Round the `price_per_kg` to 2 decimal places.

Order results by `price_per_kg` ascending, then by `name` ascending.

**`products table schema`**

* `id` (int)
* `name` (string)
* `price` (float)
* `stock` (int)
* `weight` (float)
* `producer` (string)
* `country` (string)

**`results table schema`**

* `name` (string)
* `weight` (float)
* `price` (float)
* `price_per_kg` (float)
