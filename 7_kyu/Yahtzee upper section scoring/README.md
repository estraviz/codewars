# Yahtzee upper section scoring

## Introduction

The game of Yahtzee is played by rolling five 6-sided dice, and scoring the results in a number of ways. For the purpose of this kata, the upper section of Yahtzee gives you six possible ways to score a roll. 1 times the number of 1s in the roll, 2 times the number of 2s, 3 times the number of 3s, and so on up to 6 times the number of 6s. For instance, consider the roll `[2, 3, 5, 5, 6]`. If you scored this as 1s, the score would be 0, since there are no 1s in the roll. If you scored it as 2s, the score would be 2, since there's one 2 in the roll. Scoring the roll in each of the six ways gives you the six possible scores: `0 2 3 0 10 6`. The maximum here is 10 (2x5), so your result should be 10.

You are given a Yahtzee dice roll, represented as a list with `k` integers from `1` to `10000`. Your task is to find the maximum possible score for this roll in the upper section of the Yahtzee score card. Here's what that means.

## Examples

```markdown
yahtzee_upper([2, 3, 5, 5, 6]) => 10 #5*2=10 - there is two numbers 5, and that gives as 10
yahtzee_upper([1, 1, 1, 1, 3]) => 4  #1*4=4, while 3*1=3 - there is four numbers 1, and that gives as 4, while one number 3 gives as 3
yahtzee_upper([1, 1, 1, 3, 3]) => 6
yahtzee_upper([15, 9, 9, 8, 9]) => 27
yahtzee_upper([1654, 1654, 5099, 3086, 1654, 5099, 2274,
    1654, 1654, 1654, 1654, 1654, 3086, 4868, 1654, 4868, 1654,
    3086, 4868, 3086]) => 16540 #1654*10=16540 - large example - there is ten numbers 1654, and that gives as 16540
```

## Limitations

The tests will use following numbers:

Number of rolls: `50 < k < 5000`
