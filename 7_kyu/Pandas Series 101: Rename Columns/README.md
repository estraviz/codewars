# Pandas Series 101: Rename Columns

## Description

### Input parameters

1. `pandas.DataFrame` object.
2. sequence.

### Task

Your function must return a new `pandas.DataFrame` object with same data than the original input but now its column names are the elements of the sequence. You must not modify the original input.

The number of columns of the input will always be equal to the size of the sequence.

### Examples

```python
   0  1  2
0  1  2  3
1  4  5  6

names = ['A', 'B', 'C']
```

```python
   A  B  C
0  1  2  3
1  4  5  6
```
