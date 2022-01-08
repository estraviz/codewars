# Birthday I - Cake

## Description

It's your birthday. Your colleagues buy you a cake. The numbers of candles on the cake is provided (`candles`). Please note this is not reality, and your age can be anywhere up to 1000. Yes, you would look a mess.

As a surprise, your colleagues have arranged for your friend to hide inside the cake and burst out. They pretend this is for your benefit, but likely it is just because they want to see you fall over covered in cake. Sounds fun!

When your friend jumps out of the cake, he/she will knock some of the candles to the floor. If the number of candles that fall is higher than 70% of total candles, the carpet will catch fire.

You will work out the number of candles that will fall from the provided lowercase string (`debris`). You must add up the character ASCII code of each _even indexed_ (assume a 0 based indexing) character in the string, with the alphabetical position ("a" = 1, "b" = 2, etc.) of each _odd indexed_ character to get the string's total.

For example:

```python
"abc"  -->  "a" = 97, "b" = 2, "c" = 99  -->  total = 198
```

If the carpet catches fire, return `"Fire!"`, if not, return `"That was close!"`.

## Notes

* if there are no candles to begin with, the carpet cannot catch fire;
* as this is not reality, you may have more candles falling from the cake than the total...
