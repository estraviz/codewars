# Histogram - H1

## Description

![kata](./img/kata.png "A Weekly Coding Challenge featured Kata")

**See also**

* [Histogram - V1](https://www.codewars.com/kata/57c6c2e1f8392d982a0000f2)

### Background

A 6-sided die is rolled a number of times and the results are plotted as a character-based histogram.

Example:

```python
6|##### 5
5|
4|# 1
3|########## 10
2|### 3
1|####### 7
```

### Task

You will be passed the dice value frequencies, and your task is to write the code to return a string representing a histogram, so that when it is printed it has the same format as the example.

### Notes

* There are no trailing spaces on the lines.
* All lines (including the last) end with a newline `\n`.
* A count is displayed beside each bar except where the count is 0.
* The number of rolls may vary but there are never more than 100.
