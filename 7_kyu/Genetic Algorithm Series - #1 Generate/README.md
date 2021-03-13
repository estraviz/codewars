# Genetic Algorithm Series - #1 Generate

## Description

A genetic algorithm is based in groups of chromosomes, called populations. To start our population of chromosomes we need to generate random binary strings with a specified length.

In this kata you have to implement a function `generate` that receives a `length` and has to return a random binary strign with `length` characters.

![sequence](img/sequence.gif)

### Example

Generate a chromosome with length of 4 `generate(4)` could return the chromosome `0010`, `1110`, `1111`... or any of 2<sup>4</sup> possibilities.

_**Note:** Some tests are random. If you think your algorithm is correct but the result fails, trying again should work._
