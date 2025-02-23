from typing import TypeVar, Sequence, Optional, TYPE_CHECKING
from decimal import Decimal


if TYPE_CHECKING:
    from .currency.base import _Currency
else:
    _Currency = "_Currency"


Currency = TypeVar("Currency", bound=_Currency)


def convert(value: Currency, currency: type[Currency]) -> Currency:
    """Converts the currency object using pre-configured conversion rates
    
    :param value: Currency object
    :param currency: New currency class to be converted to"""
    rate = currency._get_convertion_rate(value.__class__)
    new_value = value.as_decimal() * Decimal(rate)
    new_value_as_subunit = int(new_value * 10 ** currency._subunit_size)
    return currency._new_from_subunit(new_value_as_subunit)


def _sum(
    items: Sequence[Currency], cls: Optional[type[Currency]] = None
) -> Currency:
    """Equivalent to builtin `sum`.

    Recieves a sequence of values of the same currency, and returns an instance
    of the same type. Raises error if sequence contains objects of different
    types.

    :param items: Sequence of objects of same currency
    :param cls: Currency class expected
    """
    t = items.__class__
    if cls is None:
        try:
            cls = items[0].__class__
        except IndexError:
            raise ValueError("Can't infer Currency class from empty sequence")
    acc = 0
    for i, item in enumerate(items):
        if item.__class__ != cls:
            raise ValueError(
                "Sum aborted. "
                f"{t} contains items of types {cls} and {item.__class__}"
            )
        acc += item._value

    return cls._new_from_subunit(acc)


def _mean(
    items: Sequence[Currency], cls: Optional[type[Currency]] = None
) -> Currency:
    """Arithmetic mean of a Currency sequence. Better if called from a class
    method.

    :param items: Sequence of objects of same currency
    :param cls: Currency class expected
    """
    empty_error = ValueError("Can't find the mean value of empty list")
    if cls is None:
        try:
            cls = items[0].__class__
        except IndexError:
            raise empty_error
    total = cls.sum(items)
    try:
        return total / len(items)
    except ZeroDivisionError:
        raise empty_error
