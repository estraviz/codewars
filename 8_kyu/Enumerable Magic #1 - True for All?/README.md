# Enumerable Magic #1 - True for All?

## Description

Create a method **all** which takes two params:

* a sequence,
* a function (function pointer in C),

and returns true if the function in the params returns true for every element in the sequence. Otherwise, it should return false. If the sequence is empty, it should return true, since technically nothing failed the test.

## Example

```python
all((1, 2, 3, 4, 5), greater_than_9) -> false
all((1, 2, 3, 4, 5), less_than_9)    -> True
```
