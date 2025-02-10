from typing import TypeVar, Sequence, TYPE_CHECKING


if TYPE_CHECKING:
    from .base import _Currency
else:
    _Currency = "_Currency"


Currency = TypeVar("Currency", bound=_Currency)


def sum_(items: Sequence[Currency]) -> Currency:
    """Equivalent to builtin `sum`.

    Recieves a sequence of values of the same currency, and returns an instance
    of the same type. Raises error if sequence is empty or contains objects of
    different types.

    :param items: Sequence of objects of same currency
    """
    t = items.__class__
    try:
        cls = items[0].__class__
    except IndexError:
        raise ValueError(f"Can't sum empty {t}")
    acc = 0
    for i, item in enumerate(items):
        if i == 0:
            cls = item.__class__
        elif item.__class__ != cls:
            raise ValueError(
                "Sum aborted. "
                f"{t} contains items of types {cls} and {item.__class__}"
            )
        acc += item._value

    return cls._new_from_subunit(acc)
