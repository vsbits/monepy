# Monepy

[![tests](https://github.com/vsbits/monepy/actions/workflows/tests.yml/badge.svg)](https://github.com/vsbits/monepy/actions/workflows/tests.yml)
[![Codecov](https://img.shields.io/codecov/c/github/vsbits/monepy?logo=codecov&label=coverage)](https://codecov.io/gh/vsbits/monepy)

[![PyPI - Version](https://img.shields.io/pypi/v/monepy?logo=pypi&color=blue)](https://pypi.org/project/Monepy/)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/vsbits/monepy/blob/main/LICENSE)

A python package that implements currency classes to work with monetary values.

It behaves like a numeric class under the hood is an easy way to work with
money:

```
>>> from monepy import USD
>>> x = USD(500)
>>> x
<USD 500.00>
>>> x = USD(500)
>>> y = USD(25)
>>> x > y
True
>>> z = x + y
>>> z
<USD 525.00>
>>> print(f"Total is {z.formatted()}")
Total is $525.00
```

## Documentation

The full documentation of the module is available at [here](https://vsbits.net/monepy).

