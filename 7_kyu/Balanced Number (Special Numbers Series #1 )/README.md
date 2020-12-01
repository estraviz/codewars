# Balanced Number (Special Numbers Series #1 )

## Description

A **balanced number** is the number that satisfies that the sum of all digits to the left of the middle digit(s) and the sum of all digits to the right of the middle digit(s) are equal.

## Task

Given a number, find if it is **"Balanced"** or **"Not Balanced"**.

## Notes

* If the number has an odd number of digits then there is only one middle digit, e.g. `92645` has middle digit `6`; otherwise, there are two middle digits, e.g. `1301` has middle digits `3` and `0`.

* The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g `413023` is a balanced number because the left sum and right sum are both `5`.
* Number passed is always positive.
* Return the result as String

## Input >> Output Examples

```python
balanced_num(7) ==> return "Balanced"
```

#### Explanation:

* Since the sum of all digits to the left of the middle digit (0)
* and the sum of all digits to the right of the middle digit (0) are equal then it's balanced.

---

```python
balanced_num(295591) ==> return "Not Balanced"
```

#### Explanation:

* Since the sum of all digits to the left of the middle digits (11)
* and the sum of all digits to the right of the middle digits (10) are not equal then it's not balanced.
* Note : The middle digit(s) are 55.

---

```python
balanced_num(959) ==> return "Balanced"
```

#### Explanation:

* Since the sum of all digits to the left of the middle digits (9)
* and the sum of all digits to the right of the middle digits (9) are equal then it's balanced.
* Note : The middle digit is 5 .

---

```python
balanced_num(27102983) ==> return "Not Balanced"
```

#### Explanation:

* Since the sum of all digits to the left of the middle digits (10)
* and the sum of all digits to the right of the middle digits (20) are not equal then it's not balanced.
* Note : The middle digit(s) are 02 .
