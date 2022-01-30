# Construct a bit vector set

## Description

Write a function which accepts a sequence of unique integers as argument and returns a 32-bit integer such that the integer, in its binary representation has `1` at only those indexes (counted from right) which are in the sequence.

## Examples

```python
sort_by_bit([0, 1]) # Returns integer 3
sort_by_bit([1, 2, 0, 4]) # Returns integer 23
```

FAQ: The function name contains `sort` as it simulates [radix sort](https://en.wikipedia.org/wiki/Radix_sort).
