# Spraying trees

## Description

There are five workers: `James`, `John`, `Robert`, `Michael` and `William`. They work one by one and on weekends they rest. Order is same as in the description (James works on mondays, John works on tuesdays and so on). You have to create a function `'task'` that will take 3 arguments(`w, n, c`):

1. Weekday.
2. Number of trees that must be sprayed on that day.
3. Cost of 1 litre liquid that is needed to spray tree,let's say one tree needs 1 litre liquid.

Let cost of all liquid be `x`.

Your function should return string like this: `'It is (weekday) today, (name), you have to work, you must spray (number) trees and you need (x) dollars to buy liquid'`.

**For example:**

```python
task('Monday',15,2) -> 'It is Monday today, James, you have to work, you must spray 15 trees and you need 30 dollars to buy liquid'
```
