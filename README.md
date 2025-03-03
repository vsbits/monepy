# Monepy

[![tests](https://github.com/vsbits/monepy/actions/workflows/tests.yml/badge.svg)](https://github.com/vsbits/monepy/actions/workflows/tests.yml)
[![Codecov](https://img.shields.io/codecov/c/github/vsbits/monepy?logo=codecov&label=coverage)](https://codecov.io/gh/vsbits/monepy)

[![PyPI - Version](https://img.shields.io/pypi/v/monepy?logo=pypi&color=blue)](https://pypi.org/project/Monepy/)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/vsbits/monepy/blob/main/LICENSE)

A python package that implements currency classes to work with monetary values.

## Install

From PyPI using `pip`:

```
pip install monepy
```

## Behavior

The currency classes behave like a numeric type, with a `formatted()` method
that returns the value in the currency format:

```
>>> from monepy import USD
>>> x = USD(10)
>>> x
<USD 10.00>
>>> x.formatted()
'$10.00'
```

The class constructor does not round the values recieved. If a value with more 
significant digits than the currency supports is provided, a `ValueError` will
be raised.

### Operators

Arithmetic operators are supported with numeric values and same currency
objects, as follows:

#### The `+` and `-`

Operations with `+` and `-` can only be done with currencies of the same type
and will return an object of the same currency:

```
>>> x = USD(10)
>>> y = USD(0.1)
>>> x + y
<USD 10.10>
>>> x - y
<USD 9.90>
```

#### The `*`

The `*` is only possible with a numeric value:

```
>>> x = USD(1.99)
>>> x * 1.23
<USD 2.44>
```

#### The `/`, `//` and `%`
Division related operators are possible with numeric and currencies of the same
type:

```
>>> x = USD(10)
>>> y = USD(3)
>>> x / y
3.3333333333333335
>>> x // y
3
>>> x % y
<USD 1.00>
```

Since currencies have a smallest unit size, any division by a numeric value
will have the same return regardless of the operator

```
>>> x = USD(10)
>>> x / 3
<USD 3.33>
>>> x // 2
<USD 3.33>
>>> x % 3
<USD 0.01>
```

### Pandas integration

Currency classes can be used with the [pandas library](https://pandas.pydata.org/):

```
>>> import pandas as pd
>>> from monepy import EUR
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
>>> df["price"] = df["price"].map(EUR, na_action="ignore")
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
>>> df[df["price"] >= EUR(10)]
  product  price  quantity  subtotal
0       x  10,00         8     80,00
2       z  25,00       200  5 000,00
>>> total = df["subtotal"].sum()
>>> print(f"The total is {total.formatted()}.")
The total is 5 129,50 €.
```
