# All Star Code Challenge #15

## Description

Your family runs a shop and have just brought a [Scrolling Text Machine](./img/l-e-d-multicolour-text-board-250x250.jpeg/l-e-d-multicolour-text-board-250x250.jpg) to help get some more business.

The scroller works by replacing the current text string with a similar text string, but with the first letter shifted to the end; this simulates movement.

You're father is far too busy with the business to worry about such details, so, naturally, he's making you come up with the text strings.

Create a function named `rotate()` that accepts a string argument and returns an array of strings with each letter from the input string being rotated to the end.

```python
rotate("Hello") // => ["elloH", "lloHe", "loHel", "oHell", "Hello"]
```

**Note:** The original string should be included in the output array The order matters. Each element of the output array should be the rotated version of the previous element. The output array SHOULD be the same length as the input string The function should return an emptry array with a 0 length string, '', as input.
