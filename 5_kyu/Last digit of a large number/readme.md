# Last digit of a large number

## Description

Define a function that takes in two non-negative integers `a` and `b` and returns the last decimal digit of `a`<sup>`b`</sup>. Note that `a` and `b` may be very large!

For example, the last decimal digit of `9`<sup>`7`</sup> is `9`, since `9`<sup>`7`</sup>` = 4782969`. The last decimal digit of `(2`<sup>`200`</sup>`)`<sup>`(2`<sup>`300`</sup>`)`</sup>, which has over `10`<sup>`92`</sup> decimal digits, is `6`. Also, please take `0`<sup>`0`</sup> to be `1`.

You may assume that the input will always be valid.

## Examples

```python
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
```

## Remarks

### JavaScript, C++, R, PureScript

Since these languages don't have native arbitrarily large integers, your arguments are going to be strings representing non-negative integers instead.
