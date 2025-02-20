from typing import Self, Union, overload, Optional, Any, Sequence
from decimal import Decimal
from ..utils import _sum, _mean


class _Currency:
    """Class to reprensent a currency.

    Should not be direcly instanciated."""

    _value: int
    """Stored value in the smallest unit for the selected currency.

    e.g.: cents for USD"""
    _symbol: str
    """Symbol used to represent the formatted currency.

    '$', '€', '¥' etc"""
    _symbol_space: bool
    """Tells if there should me a space separating the symbol from the value"""
    _symbol_begining: bool
    """Tells if the symbol should be before the value, otherwise is appended
    at the end."""
    _thousand_sep: str
    """Character used to separate each thousant unit"""
    _subunit_size: int
    """How many significant digits the currency has for its subunit

    e.g: 2 for EUR (1,00 €) and 0 for JPY (¥ 1)"""
    _subunit_sep: Optional[str]
    """Character used to separate currency unit form subunit. None if
    `subunit_sep == 0`."""

    def __init__(self, value: Union[int, float]):
        """Instatiates a new Currency object.

        e.g.

        .. code-block:: python

           >>> EUR(1.5)
           <EUR 1,50>

        :param value: unit value of the currency. If it has more significant
            digits than the currency supports, will raise ``ValueError``
        """
        if isinstance(value, int):
            self._value = value * 10**self._subunit_size
        elif isinstance(value, float):
            decimal_places = Decimal(str(value)).as_tuple().exponent
            if isinstance(decimal_places, int) and (
                -decimal_places <= self._subunit_size
            ):
                self._value = int(value * 10**self._subunit_size)
            else:
                raise ValueError(
                    f"invalid value <{value}>. {type(self)} suports only"
                    f" {self._subunit_size} decimal places"
                )
        else:
            raise ValueError(f"invalid value for {type(self)} <{type(value)}>")

    def __str__(self) -> str:
        chars = str(abs(self._value)).zfill(self._subunit_size + 1)
        rev = [char for char in chars]
        rev.reverse()
        value_as_str = ""
        for i, n in enumerate(rev, 0):
            if i == self._subunit_size:
                if self._subunit_sep is not None:
                    value_as_str = self._subunit_sep + value_as_str

            elif (i - self._subunit_size) % 3 == 0:
                value_as_str = self._thousand_sep + value_as_str

            value_as_str = n + value_as_str

        if self._value < 0:
            value_as_str = "-" + value_as_str
        return value_as_str

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.__str__()}>"

    def __hash__(self) -> int:
        return hash((self.__class__.__name__, self._value))

    def __eq__(self, other: object) -> bool:
        if self._is_currency(other):
            if self._is_same_currency(other) and isinstance(
                other, self.__class__
            ):
                return self._value == other._value
            else:
                raise NotImplementedError(
                    "Can't compare objects of classes "
                    f"{type(self)} and {type(other)}"
                )
        elif isinstance(other, (int, float)):
            return self._value / (10**self._subunit_size) == other
        return False

    def __gt__(self, other: object) -> bool:
        if self._is_currency(other):
            if self._is_same_currency(other) and isinstance(
                other, self.__class__
            ):
                return self._value > other._value
        elif isinstance(other, (int, float)):
            return self._value / (10**self._subunit_size) > other
        raise NotImplementedError(
            f"Can't compare objects of classes {type(self)} and {type(other)}"
        )

    def __ge__(self, other: object) -> bool:
        if self._is_currency(other):
            if self._is_same_currency(other) and isinstance(
                other, self.__class__
            ):
                return self._value >= other._value
        elif isinstance(other, (int, float)):
            return self._value / (10**self._subunit_size) >= other
        raise NotImplementedError(
            f"Can't compare objects of classes {type(self)} and {type(other)}"
        )

    def __lt__(self, other: object) -> bool:
        if self._is_currency(other):
            if self._is_same_currency(other) and isinstance(
                other, self.__class__
            ):
                return self._value < other._value
        elif isinstance(other, (int, float)):
            return self._value / (10**self._subunit_size) < other
        raise NotImplementedError(
            f"Can't compare objects of classes {type(self)} and {type(other)}"
        )

    def __le__(self, other: object) -> bool:
        if self._is_currency(other):
            if self._is_same_currency(other) and isinstance(
                other, self.__class__
            ):
                return self._value <= other._value
        elif isinstance(other, (int, float)):
            return self._value / (10**self._subunit_size) <= other
        raise NotImplementedError(
            f"Can't compare objects of classes {type(self)} and {type(other)}"
        )

    def __neg__(self) -> Self:
        return self._new_from_subunit(-self._value)

    def __abs__(self) -> Self:
        return self._new_from_subunit(abs(self._value))

    def __add__(self, other: Self) -> Self:
        if self._is_same_currency(other):
            result = self._value + other._value
            return self._new_from_subunit(result)
        raise TypeError(
            "Can't add objects of type "
            f"{self.__class__} and {other.__class__}"
        )

    def __sub__(self, other: Self) -> Self:
        if self._is_same_currency(other):
            result = self._value - other._value
            return self._new_from_subunit(result)
        raise TypeError(
            "Can't subtract objects of type "
            f"{self.__class__} and {other.__class__}"
        )

    def __mul__(self, other: Union[int, float]) -> Self:
        if isinstance(other, (int, float)):
            result = int(self._value * other)
            return self._new_from_subunit(result)
        raise TypeError(
            "Can't multiply objects of type "
            f"{self.__class__} and {other.__class__}"
        )

    @overload
    def __truediv__(self, other: Self) -> float: ...

    @overload
    def __truediv__(self, other: Union[int, float]) -> Self: ...

    def __truediv__(
        self, other: Union[Self, int, float]
    ) -> Union[Self, float]:
        if isinstance(other, self.__class__) and self._is_same_currency(other):
            return self._value / other._value
        elif isinstance(other, (float, int)):
            div = int(self._value / other)
            return self._new_from_subunit(div)
        raise TypeError(
            "Can't divide objects of type "
            f"{self.__class__} by {other.__class__}"
        )

    def __mod__(self, other: Union[int, float]) -> Self:
        if isinstance(other, (float, int)):
            abs_s, abs_o = abs(self), abs(other)
            result = abs_s / abs_o
            diff = abs_s - (result * abs_o)
            value = self._new_from_subunit(diff._value)
            if other < 0:
                return -value
            else:
                return value
        raise TypeError(
            "Can't divide objects of type "
            f"{self.__class__} by {other.__class__}"
        )

    def __floordiv__(self):
        raise NotImplementedError(
            f"// operator not available for <{self.__class__.__name__}> class"
        )

    @classmethod
    def _new_from_subunit(cls, value: int) -> Self:
        if isinstance(value, int):
            conversion = value / 10**cls._subunit_size
            return cls(conversion)
        raise TypeError(f"Invalid type for subunit value: {type(value)}")

    def formatted(self) -> str:
        """Returns a string of the value in the currency format standard.

        e.g.

        .. code-block:: python

           >>> BRL(10).formatted()
           'R$ 10,00'
        """
        sep = " " if self._symbol_space else ""
        if self._symbol_begining:
            return f"{self._symbol}{sep}{self.__str__()}"
        else:
            return f"{self.__str__()}{sep}{self._symbol}"

    def _is_same_currency(self, other: Any) -> bool:
        return self.__class__.__mro__ == other.__class__.__mro__

    @classmethod
    def _is_currency(cls, other: Any) -> bool:
        return all(
            x in other.__class__.__dict__.keys() for x in cls.__dict__.keys()
        )

    @classmethod
    def sum(cls, values: Sequence[Self]) -> Self:
        """Equivalent to builtin ``sum``. Recieves a sequence of Currency
        instances, and returns its sum if all of them are from from the same
        class calling the method

        :param values: Sequence of ``Currency`` values

        e.g.

        .. code-block:: python

            >>> values = [USD(x) for x in (5, 6, 1.5)]
            >>> USD.sum(values)
            <USD 12.50>
        """
        return _sum(values, cls)

    @classmethod
    def mean(cls, values: Sequence[Self]) -> Self:
        """Arithmetic mean of a sequence of Currency instances.

        :param values: Sequence of ``Currency`` values

        e.g.

        .. code-block:: python

            >>> values = [USD(x) for x in (10, 10, 7)]
            >>> USD.mean(values)
            <USD 9.00>
        """
        return _mean(values, cls)
