# Row Weights

## Description

### Scenario

_**Several people** are standing in a row divided into two teams._
The _**first person**_ goes into _**team 1**_, _**the second**_ goes into _**team 2**_, _**the third**_ goes into _**team 1**_, and so on.

### Task

Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, where the first one is the total weight of team 1, and the second one is the total weight of team 2.

### Notes

* Array size is at least 1.
* All numbers will be positive.

### Input >> Output Examples

```python
row_weights([13, 27, 49])  ==>  return (62, 27)
```

**Explanation:**

The first element 62 is the total weight of team 1, and the second element 27 is the total weight of team 2.

```python
row_weights([50, 60, 70, 80])  ==>  return (120, 140)
```

**Explanation:**

The first element 120 is the total weight of team 1, and the second element 140 is the total weight of team 2.

```python
row_weights([80])  ==>  return (80, 0)
```

**Explanation:**

The first element 80 is the total weight of team 1, and the second element 0 is the total weight of team 2.
