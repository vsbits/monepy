# Currency

[![tests](https://github.com/vsbits/currency/actions/workflows/tests.yml/badge.svg)](https://github.com/vsbits/currency/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/vsbits/currency/graph/badge.svg?token=8mHqn1neMk)](https://codecov.io/gh/vsbits/currency)

A python package that implements currency classes to work with monetary values.

## Behavior

The currency classes behave like a numeric type, with a `formatted()` method
that returns the value in the currency format:


```
>>> from currency import USD
>>> x = USD(10)
>>> x
<USD 10.00>
>>> x.formatted()
'$10.00'
>>> x == 1
False
>>> x == 10
True
>>> x > 10
False
>>> x < 10.1
True
```
The class constructor does not round the values recieved. If a value with more 
significant digits than the currency supports is provided, a `ValueError` will
be raised.

### Operators

Operations with `+` and `-` can only be done with currencies of the same type
and will return an object of the same currency:

```
>>> x = USD(10)
>>> y = USD(0.1)
>>> x + y
<USD 10.10>
```

Trying `USD(10) + 1` will raise a `TypeError`.

The `*` is only possible with a numeric value:

```
>>> x = USD(1.99)
>>> x * 1.23
<USD 2.44>
```

### Pandas integration

Currency classes can be used with the [pandas library](https://pandas.pydata.org/):

```
>>> import pandas as pd
>>> from currency import EUR
>>> df = pd.DataFrame({
... "product": ["x", "y", "z"],
... "price": [10, 0.99, 25],
... "quantity": [8, 50, 200]
... })
>>> df
  product  price  quantity
0       x  10.00         8
1       y   0.99        50
2       z  25.00       200
>>> df["price"] = df["price"].apply(EUR)
>>> df
  product  price  quantity
0       x  10,00         8
1       y   0,99        50
2       z  25,00       200
>>> df["subtotal"] = df["price"] * df["quantity"]
>>> df
  product  price  quantity  subtotal
0       x  10,00         8     80,00
1       y   0,99        50     49,50
2       z  25,00       200  5 000,00
>>> total = df["subtotal"].sum()
>>> print(f"The total is {total.formatted()}.")
The total is 5 129,50 €.
```
