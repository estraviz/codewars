# Set the Clock

## Description

All clocks can have their times changed, so when a clock is going too fast or slow, the time can be changed to be correct again. Bob has a 24-hour clock (so `2:00 PM` will be `14:00` instead), on which there are two buttons -- the `H` button and the `M` button, which increase the hour and minute, respectively, by one. Given the list of buttons Bob presses and the starting time, figure out what time Bob set his clock to.

Some details:

* When the minute reaches 60 it resets to 0 **without changing the hour**.
* Hours do not have leading zeros, only minutes do.
* The hour for midnight should be 24; 0 is not used as an hour.

It is guaranteed that:

* There are no more than 59 `'M'`s and 23 `'H'`s that Bob presses.
* The time given as the starting time will always be a valid 24-hr time.

### Examples

```python
set_clock("9:21", ['M', 'M', 'M', 'M', 'H', 'H', 'M'])                                     => "11:26"
set_clock("16:54", ['M', 'M', 'H', 'M', 'M', 'H', 'H', 'H', 'M', 'H', 'H', 'M', 'H', 'H']) => "24:00"
```
