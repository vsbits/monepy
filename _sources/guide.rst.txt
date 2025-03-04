User guide
==========

This guide covers the the basic usage of the ``Monepy`` currency classes.

Installation
------------

Monepy can be installed from PyPI using ``pip``:

   .. code-block::

      pip install monepy

After installation, the currency classes can be imported from the ``monepy``
module:


   .. code-block:: python

      >>> from monepy import USD
      >>> x = USD(10)
      >>> x
      <USD 10.00>
      >>> x.formatted()
      '$10.00'

A list of all available classes can be foun `here <api.html#available-classes>`_

Instance behavior
-----------------

Instances of a currency should behave like numeric objects when comparing
between each other:

   .. code-block:: python

      >>> from monepy import USD
      >>> x = USD(10)
      >>> y = USD(15)
      >>> x == y
      False
      >>> y <= y
      True

Operations
^^^^^^^^^^

Arithmetic operators are supported with numeric values and same currency
objects, as follows:


The ``+`` and ``-``
+++++++++++++++++++

Operations with ``+`` and ``-`` can only be done with currencies of the same type
and will return an object of the same currency:

   .. code-block:: python

      >>> x = USD(10)
      >>> y = USD(0.1)
      >>> x + y
      <USD 10.10>
      >>> x - y
      <USD 9.90>


The ``*``
+++++++++

The ``*`` is only possible with a numeric value:

   .. code-block:: python

      >>> x = USD(1.99)
      >>> x * 1.23
      <USD 2.44>


The ``/``, ``//`` and ``%``
+++++++++++++++++++++++++++

Division related operators are possible with numeric and currencies of the same
type:

   .. code-block:: python

      >>> x = USD(10)
      >>> y = USD(3)
      >>> x / y
      3.3333333333333335
      >>> x // y
      3
      >>> x % y
      <USD 1.00>

Since currencies have a smallest unit size, any division by a numeric value
will have the same return regardless of the operator

   .. code-block:: python

      >>> x = USD(10)
      >>> x / 3
      <USD 3.33>
      >>> x // 2
      <USD 3.33>
      >>> x % 3
      <USD 0.01>


Curreny conversion
------------------

It is possible to make conversions from one currency to another, but some
configuration is needed.


Setting up exchange rates
^^^^^^^^^^^^^^^^^^^^^^^^^

For conversion to be possible, you must first configure the currency class with
the exchange rates to be used.

There is no connection to any API *yet*, so the requests must be configured and
made by the user.

The section of the json response with the correct rates can then be passed to
the right currency using the ``set_rates`` method:

   .. code-block:: python

      >>> from monepy import JPY
      >>> JPY.set_rates({"EUR": 0.0063957, "USD": 0.0067021})


Converting currencies
^^^^^^^^^^^^^^^^^^^^^

After this, it is possible to use the ``JPY`` class to convert to, and from,
``USD`` and ``EUR``:

   .. code-block:: python

      >>> from monepy import USD, EUR
      >>> JPY.from_conversion(USD(1000))
      <JPY 149,206>
      >>> USD.from_conversion(JPY(150000))
      <USD 1,005.31>


Using a base currency
^^^^^^^^^^^^^^^^^^^^^

After the previous configuration, it is also possible to convert between
``USD`` and ``EUR`` using ``JPY`` as a base currency:

   .. code-block:: python

      >>> USD.from_conversion(EUR(1000), base=JPY)
      <USD 1,047.90>


Other tools
-----------

A complete list of `available methods <api.html#currency-classes>`_  and some
other tools, like `functions <api.html#utils>`_ to work with currency classes,
can be found in the `API reference <api.html>`_.


Pandas integration
------------------

Currency classes can be used with the `pandas library <https://pandas.pydata.org/>`_:

.. code-block:: python

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
