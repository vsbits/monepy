API Reference
=============

.. module:: monepy

Currency classes
----------------

All currency classes inherit methods from a base Currency class.

A list of available currency classes can be found
:ref:`here <available-classes>`.

Base methods
^^^^^^^^^^^^

The following methods are for use with the currency instance:

.. autofunction:: monepy.currency.base._Currency.formatted
.. autofunction:: monepy.currency.base._Currency.as_decimal

Class methods
^^^^^^^^^^^^^

.. autofunction:: monepy.currency.base._Currency.sum
.. autofunction:: monepy.currency.base._Currency.mean
.. autofunction:: monepy.currency.base._Currency.set_rates
.. autofunction:: monepy.currency.base._Currency.from_conversion


Utils
-----

Those are available functions to use with Currency classes, and can be imported
from ``monepy.utils``.

e.g.:

   .. code-block:: python

      >>> from monepy.utils import convert
      ...  # Import currencies and set conversion rates
      >>> convert(USD(10), EUR)
      <EUR 9,49>

.. automodule:: monepy.utils
   :members:

.. autosummary::
   :toctree: generated


.. _available-classes:

Available classes
-----------------

These currency classes can be imported directly from the ``monepy`` module:

   .. code-block:: python

      >>> from monepy import USD
      >>> x = USD(10)
      >>> x
      <USD 10.00>


.. automodule:: monepy.currency
   :members: