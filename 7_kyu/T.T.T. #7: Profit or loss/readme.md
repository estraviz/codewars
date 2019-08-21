# T.T.T. #7: Profit or loss

## Story
John runs a shop, bought some goods, and then sells them. He used a special accounting method, like this:

```python
[[60, 20], [60, -20]]
```

Each sub array records the commodity price and profit/loss to sell (percentage). Positive mean profit and negative means loss.

In the example above,

* John's first commodity sold at a price of $60, he made a profit of 20%;
* second commodities are sold at a price of $60 too, but he lost 20%.

Please calculate, whether his account is profit or loss in the end?

## Rules

Write a function ```profit_loss```, argument ```records``` is the list of sales.

Return a number (positive or negative), round to two decimal places.

## Some examples

In the example above:

```python
profit_loss([[60, 20], [60, -20]]) should return -5
```

Because:

* the cost of the first commodity is 50,
* the cost of the second commodity is 75,
* the total cost is: 50+75=125

Selling price is:  60 + 60 = 120

So the end result is 120 - 125 = -5. He made a loss of $5.

```python
profit_loss([[100,20],[80,-20]]) should return -3.33
profit_loss([[60,100],[60,-50]]) should return -30
profit_loss([[60,0],[60,0]]) should return 0
```
