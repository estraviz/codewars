# Shared Bit Counter

## Description

Complete the method that returns `True` if 2 integers share at least two `1` bits, otherwise return `False`. For simplicity assume that all numbers are non-negative.

### Examples

```python
 7  =  0111 in binary
10  =  1010
15  =  1111
```

* `7` and `10` share only a single `1`-bit (at index 2) --> `False`
* `7` and `15` share 3 `1`-bits (at indexes 1, 2, and 3) --> `True`
* `10` and `15` share 2 `1`-bits (at indexes 0 and 2) --> `True`

_Hint:_ you can do this with just string manipulation, but binary operators will make your life much easier.
