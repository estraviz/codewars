# Form The Largest

## Description

Given a number `n`, return the maximum number that could be formed from the digits of the number given.

## Notes

Only Natural numbers passed to the function. Numbers contain digits [0:9] inclusive.

Digit duplications could occur, so also consider it when forming the largest.

## Input >> Output Examples

```python
maxNumber (213) ==> return (321)
```

Explanation:
As `321` is the maximum number that could be formed from the digits of the number `213`.

```python
maxNumber (7389) ==> return (9873)
```

Explanation:
As `9873` is the maximum number that could be formed from the digits of the number `7389`.

```python
maxNumber (63729) ==> return (97632)
```

Explanation:
As `97632` is the maximum number that could be formed from the digits of the number `63729`.

```python
maxNumber (566797) ==> return (977665)
```

Explanation:
As `977665` is the maximum number that could be formed from the digits of the number `566797`.

Note : Digit duplications are considered when forming the largest number.

```python
maxNumber (17693284) ==> return (98764321)
```

Explanation:
As `98764321` is the maximum number that could be formed from the digits of the number `17693284`.
