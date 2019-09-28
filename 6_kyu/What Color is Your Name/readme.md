# What Color is Your Name

## Description

**Do names have colors?**

_Now they do._

Make a function that takes in a name (Any string two chars or longer really, but the name is the idea) and use the ascii values of it's substrings to produce the hex value of its color! Here is how it's going to work:

* The first two hexadecimal digits are the SUM of the value of characters (modulo 256).
* The second two are the _PRODUCT_ of all the characters (again, modulo 256, which is one more than `FF` in hexadecimal).
* The last two are the _ABSOLUTE VALUE_ of the _DIFFERENCE_ between the first letter, and the sum of every other letter. (I think you get the idea with the modulo thing).

For example `"Jack"` returns `"79CAE5"`, which is... <span style="color:#79CAE5; font-weight:bold;">baby blue!</span>

```python
"Jack"  #  "J" = 74, "a" = 97, "c" = 99, "k" = 107

74 + 97 + 99 + 107 = 377                   -->  mod 256 = 121  -->  hex: 79
74 * 97 * 99 * 107 = 76036554              -->  mod 256 = 202  -->  hex: CA
74 - (97 + 99 + 107) = -229  --> abs: 229  -->  mod 256 = 229  -->  hex: E5
```

NOTE: The function should return `None/nil` when the input is less than two chars.

