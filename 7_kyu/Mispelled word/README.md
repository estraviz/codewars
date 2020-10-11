# Mispelled word

## Description

Create a function `mispelled(word1, word2)`:

```python
mispelled('versed', 'xersed')  # returns True
mispelled('versed', 'applb')  # returns False
mispelled('versed', 'v5rsed')  # returns True
mispelled('1versed', 'versed')  # returns True
```

It checks if the word2 differs from word1 by only one character.

This can include an extra char at the end or the beginning of either of words.

In the tests that expect `True`, the mispelled word will always differ only by one character.

The only exception to the rule above is if one string is empty, in that case, it should return `False` (if both strings are empty, then return `True`).
