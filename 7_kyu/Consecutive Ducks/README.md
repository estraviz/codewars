# Consecutive Ducks

## Description

Positive integers have so many gorgeous features. Some of them could be expressed as a sum of two or more consecutive positive numbers.

Consider an example:

`10`, could be expressed as a sum of `1 + 2 + 3 + 4`.

## Task

Given a positive integer, `N`, Return `True` if it could be expressed as a sum of two or more consecutive positive numbers, otherWise return `False`.

## Notes

Guaranteed constraint: `2 ≤ N ≤ (2^32) - 1`.

## Input >> Output Examples

```python
* consecutiveDucks(9)   ==>  return True  as  9 could be expressed as a sum of ( 2 + 3 + 4 ) or ( 4 + 5 ).
* consecutiveDucks(64)  ==>  return False
* consecutiveDucks(42)  ==>  return True  as 42 could be expressed as a sum of ( 9 + 10 + 11 + 12 ).
```
