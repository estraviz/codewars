# Negation of a Value

## Description

In programming you know the use of the logical negation operator (`!`), it reverses the meaning of a condition.

```python
!false = true
!!false = false
```

Your task is to complete the function `negation_value()` that takes a string of negations with a value and returns what the value would be if those negations were applied to it.

```python
negation_value("!", False) #=> True
negation_value("!!!!!", True) #=> False
negation_value("!!", []) #=> False
```

Do **not** use the `eval()` function or the Function() constructor in JavaScript.

_Note: Always return a boolean value, even if there're no negations._
