from typing import TypeVar, Sequence, Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from .currency.base import _Currency
else:
    _Currency = "_Currency"


Currency = TypeVar("Currency", bound=_Currency)


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
