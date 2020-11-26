# Consecutive letters

## Description

In this Kata, we will check if a string contains consecutive letters as they appear in the English alphabet and if each letter occurs only once.

Rules are:

1. The letters are adjacent in the English alphabet.
2. Each letter occurs only once.

For example:

```python
solve("abc") = True, because it contains a,b,c
solve("abd") = False, because a, b, d are not consecutive/adjacent in the alphabet, and c is missing.
solve("dabc") = True, because it contains a, b, c, d
solve("abbc") = False, because b does not occur once.
solve("v") = True
```

All inputs will be lowercase letters.
