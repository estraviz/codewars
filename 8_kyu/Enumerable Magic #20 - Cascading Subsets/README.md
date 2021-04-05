# Enumerable Magic #20 - Cascading Subsets

## Description

Create a method `each_cons` that accepts a list and a number `n`, and returns cascading subsets of the list of size `n`, like so:

```python
each_cons([1,2,3,4], 2)
  #=> [[1,2], [2,3], [3,4]]

each_cons([1,2,3,4], 3)
  #=> [[1,2,3],[2,3,4]]
```

As you can see, the lists are cascading; ie, they overlap, but never out of order.
