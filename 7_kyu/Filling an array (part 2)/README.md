# Filling an array (part 2)

## Description

Following on from [Part 1](https://github.com/estraviz/codewars/tree/master/8_kyu/Filling%20an%20array%20(part%201)), part 2 looks at some more complicated array contents.

So let's try filling an array with...

### ...square numbers
The numbers from `1` to `n*n`:

```python
const squares = n => ???
squares(5) // [1, 4, 9, 16, 25]
```

### ...a range of numbers
A range of numbers starting from `start` and increasing by `step`:

```python
const range = (n, start, step) => ???
range(6, 3, 2) // [3, 5, 7, 9, 11, 13]
```

### ...random numbers
A bunch of random integers between `min` and `max`:

```python
const random = (n, min, max) => ???
random(4, 5, 10) // [5, 9, 10, 7]
```

### ...prime numbers
All primes starting from `2` (obviously)...:

```python
const primes = n => ???
primes(6) // [2, 3, 5, 7, 11, 13]
```

**Note:** All the above functions should take as their first parameter a number that determines the length of the returned array.
