# Electronics #1. Ohm's Law

This is based on [Ohm's Law](https://en.wikipedia.org/wiki/Ohm%27s_law): `V = IR`, being:

* `V`: Voltage in volts (V).
* `I`: Current in amps (A).
* `R`: Resistance in ohms (R).

## Task

Create a function `ohms_law(s)` that has an input string.

* Your get a string in the form: `'2R 10V'` or `'1V 1A'`, for example.
* Each value of magnitude in the string will be expressed in `'V'`, `'A'` or `'R'`.
* Each value is separated by a space bar in the string.
* You must return a string with the value of missing magnitude followed by the unit (`'V'`, `'A'`, `'R'`).
* That value will be rounded to six (6) decimals.

## Examples

```python
'25V 1e-2A' --> '2500.0R'
'2200R 5V' --> '0.002273A'
'3.3e-3A 1e3R' --> '3.3V'
```

## Inputs

All inputs will be valid, no need to check them.
