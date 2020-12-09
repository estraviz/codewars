# L2: Triple X

## Description

Given a string, return true if the first instance of `x` in the string is immediately followed by the string `xx`.

```python
tripleX("abraxxxas") → True
tripleX("xoxotrololololololoxxx") → False
tripleX("softX kitty, warm kitty, xxxxx") → True
tripleX("softx kitty, warm kitty, xxxxx") → False
```

### Note

* Capital X's do not count as an occurrence of `x`.
* If there are no `x`'s then return `False`.
