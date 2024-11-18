# L1: Set Alarm

## Description

Write a function named setAlarm which receives two parameters. The first parameter, _employed_, is true whenever you are employed and the second parameter, _vacation_ is true whenever you are on vacation.

The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

```python
setAlarm(true, true) -> false
setAlarm(false, true) -> false
setAlarm(false, false) -> false
setAlarm(true, false) -> true
```