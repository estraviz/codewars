# Can you find the needle in the haystack

## Description

Write a function `findNeedle()` that takes an array full of junk but containing one `"needle"`.

After your function finds the needle it should return a message (as a string) that says:

`"found the needle at position "` plus the index it found the needle, so:

Python, Ruby & Elixir:

```python
find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
```

JavaScript & TypeScript:

```javascript
findNeedle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
```

Java:

```java
findNeedle(new Object[] {"hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"})
```

should return:

`"found the needle at position 5"`.