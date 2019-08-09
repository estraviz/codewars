# The Poet And The Pendulum

## Description

### Scenario
The rhythm of beautiful musical notes is drawing a pendulum.
Beautiful musical notes are the numbers ;);)

### Task
Given an array/list [] of n integers, arrange them in a way similar to the to-and-fro movement of a Pendulum:

* The smallest element of the list of integers, must come in center position of array/list.
* The higher than smallest, goes to the right.
* The next higher number goes to the left of minimum number and so on, in a to-and-fro manner similar to that of a Pendulum.

### Notes

* Array/list size is at least 3.
* In an even array size, the minimum element should be moved to (n-1)/2 index (considering that indexes start from 0).
* Repetition of numbers in the array/list could occur, so duplications are included when arranging.

## Input >> Output Examples

### Example 1

```python
pendulum ([6, 6, 8 ,5 ,10]) ==> [10, 6, 5, 6, 8]
```

Explanation:

* Since `5` is the the smallest element of the list of integers, it came in the center position of array/list.
* The higher than smallest is `6` goes to the right of `5`.
* The next higher number goes to the left of minimum number and so on.
* Remember, duplications are included when arranging, don't delete them.

### Example 2

```python
pendulum ([-9, -2, -10, -6]) ==> [-6, -10, -9, -2]
```

Explanation:

* Since `-10` is the The Smallest element of the list of integers, it came in the center position of array/list.
* The higher than smallest is `-9` goes to the right of it.
* The next higher number goes to the left of `-10`, and so on.
* Remember, in an even array size, the minimum element moved to (n-1)/2 index (considering that indexes start from 0).

### Example 3

```python
pendulum ([11, -16, -18, 13, -11, -12, 3, 18 ]) ==> [13, 3, -12, -18, -16, -11, 11, 18]
```

Explanation:

* Since `-18` is the the smallest element of the list of integers, it came in the center position of array/list.
* The higher than smallest is `-16` goes to the right of it.
* The next higher number goes to the left of `-18`, and so on.
* Remember, in an even array size, the minimum element moved to (n-1)/2 index (considering that indexes start from 0).

**Tune your code, there are 200 assertions, 60.000 element for each.**
