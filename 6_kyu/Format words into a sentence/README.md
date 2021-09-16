# Format words into a sentence

## Description

Complete the method so that it formats the words into a single comma separated value. The last word should be separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a single formatted string. Empty string values should be ignored. Empty arrays or null/nil values being passed into the method should result in an empty string being returned.

```python
format_words(['ninja', 'samurai', 'ronin']) # should return "ninja, samurai and ronin"
format_words(['ninja', '', 'ronin']) # should return "ninja and ronin"
format_words([]) # should return ""
```
