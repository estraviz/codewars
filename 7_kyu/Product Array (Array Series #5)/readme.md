# Product Array (Array Series #5)

## Description

Given an array/list `arr` of integers, construct a product array `prod` of same size such that `prod[i]` is equal to the product of all the elements of `arr` except `arr[i]`.

## Notes

* Array/list size is at least 2.
* Array/list's numbers will be only positives.
* Repetition of numbers in the array/list could occur.

### Input >> Output Examples

**Ex. 1:**

```python
product_array ({12, 20}) ==>  return {20, 12}
```

_Explanation:_

* The first element in prod [] array 12 is the product of all array's elements except the first element.
* The second element 20 is the product of all array's elements except the second element .

**Ex. 2:**

```python
product_array ({1, 5, 2}) ==> return {10, 2, 5}
```

_Explanation:_

* The first element 10 is the product of all array's elements except the first element 1.
* The second element 2 is the product of all array's elements except the second element 5.
* The Third element 5 is the product of all array's elements except the Third element 2.

**Ex. 3:**

```python
product_array ({10, 3, 5, 6, 2}) return ==> {180, 600, 360, 300, 900}
```

_Explanation:_

* The first element 180 is the product of all array's elements except the first element 10.
* The second element 600 is the product of all array's elements except the second element 3.
* The Third element 360 is the product of all array's elements except the third element 5.
* The Fourth element 300 is the product of all array's elements except the fourth element 6.
* Finally ,The Fifth element 900 is the product of all array's elements except the fifth element 2.
