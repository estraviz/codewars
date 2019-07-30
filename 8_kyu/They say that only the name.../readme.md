# They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it series #1: Are they opposite

## Description

Give you two strings: `s1` and `s2`. If they are opposite, return True otherwise, return false. Note: The result should be a boolean value, instead of a string.

The `opposite` means: All letters of the two strings are the same, but the case is opposite. you can assume that the string only contains letters or it's a empty string. Also take note of the edge case - if both strings are empty then you should return `false`/`False`.

## Some examples

```python
is_opposite("ab", "AB") should return True
is_opposite("aB", "Ab") should return True
is_opposite("aBcd", "AbCD") should return True
is_opposite("AB", "Ab") should return False
is_opposite("", "") should return False
```
