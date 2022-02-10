# Some (but not all)

## Description

Your task is to create a function that given a sequence and a predicate, returns `True` if only some (but not all) the elements in the sequence are `True` after applying the predicate.

### Examples

```python
some('abcdefg&%$', str.isalpha)
>>> True

some('&%$=', str.isalpha)
>>> False

some('abcdefg', str.isalpha)
>>> False

some([4, 1], lambda x: x>3)
>>> True

some([1, 1], lambda x: x>3)
>>> False

some([4, 4], lambda x: x>3)
>>> False
```
