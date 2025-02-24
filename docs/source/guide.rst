User guide
==========

Instance behavior
-----------------

Operations
^^^^^^^^^^

Methods
^^^^^^^


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
