# Valid Spacing

## Description

Your task is to write a function called `valid_spacing()` or `validSpacing()` which checks if a string has valid spacing. The function should return either `True` or `False`.

For this kata, the definition of valid spacing is one space between words, and no leading or trailing spaces. Below are some examples of what the function should return.

```python
'Hello world' = True
' Hello world' = False
'Hello world  ' = False
'Hello  world' = False
'Hello' = True
# Even though there are no spaces, it is still valid because none are needed
'Helloworld' = True
# True because we are not checking for the validity of words.
'Helloworld ' = False
' ' = False
'' = True
```

_Note - there will be no punctuation or digits in the input string, only letters._
