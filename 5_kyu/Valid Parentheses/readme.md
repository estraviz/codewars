# Valid Parentheses

## Description

Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return `True` if the string is valid, and `False` if it's invalid.

## Examples

```python
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
```

## Constraints

```python
0 <= input.length <= 100
```

Along with opening `(()` and closing `())` parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. `[]`, `{}`, `<>`).
