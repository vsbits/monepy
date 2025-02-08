from typing import Self, Union, overload, Optional, Any
from decimal import Decimal


class _Currency:
    """Class to reprensent a currency.
    Should not be direcly instanciated."""

    _value: int
    """Stored value in the smallest unit for the selected currency.
    e.g.: cents for USD"""
    symbol: str
    symbol_space: bool
    symbol_begining: bool
    thousand_sep: str
    subunit_size: int
    subunit_sep: Optional[str]

    def __init__(self, value: Union[int, float]):
        if isinstance(value, int):
            self._value = value * 10**self.subunit_size
        elif isinstance(value, float):
            decimal_places = Decimal(str(value)).as_tuple().exponent
            if isinstance(decimal_places, int) and (
                -decimal_places <= self.subunit_size
            ):
                self._value = int(value * 10**self.subunit_size)
            else:
                raise ValueError(
                    f"invalid value <{value}>. {type(self)} suports only"
                    f" {self.subunit_size} decimal places"
                )
        else:
            raise ValueError(f"invalid value for {type(self)} <{type(value)}>")

    def __str__(self) -> str:
        chars = str(abs(self._value)).zfill(self.subunit_size + 1)
        rev = [char for char in chars]
        rev.reverse()
        value_as_str = ""
        for i, n in enumerate(rev, 0):
            if i == self.subunit_size:
                if self.subunit_sep is not None:
                    value_as_str = self.subunit_sep + value_as_str

            elif (i - self.subunit_size) % 3 == 0:
                value_as_str = self.thousand_sep + value_as_str

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
                    f"Can't compare objects of classes {type(self)} and {type(other)}"
                )
        elif isinstance(other, (int, float)):
            return self._value / (10**self.subunit_size) == other
        return False

    def __gt__(self, other: object) -> bool:
        if self._is_currency(other):
            if self._is_same_currency(other) and isinstance(
                other, self.__class__
            ):
                return self._value > other._value
        elif isinstance(other, (int, float)):
            return self._value / (10**self.subunit_size) > other
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
            return self._value / (10**self.subunit_size) >= other
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
            return self._value / (10**self.subunit_size) < other
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
            return self._value / (10**self.subunit_size) <= other
        raise NotImplementedError(
            f"Can't compare objects of classes {type(self)} and {type(other)}"
        )

    def __add__(self, other: Self) -> Self:
        if self._is_same_currency(other):
            result = self._value + other._value
            return self._new_from_subunit(result)
        raise TypeError(
            f"Can't add objects of type {self.__class__} and {other.__class__}"
        )

    def __sub__(self, other: Self) -> Self:
        if self._is_same_currency(other):
            result = self._value - other._value
            return self._new_from_subunit(result)
        raise TypeError(
            f"Can't subtract objects of type {self.__class__} and {other.__class__}"
        )

    def __mul__(self, other: Union[int, float]) -> Self:
        if isinstance(other, (int, float)):
            result = int(self._value * other)
            return self._new_from_subunit(result)
        raise TypeError(
            f"Can't multiply objects of type {self.__class__} and {other.__class__}"
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
            f"Can't divide objects of type {self.__class__} by {other.__class__}"
        )

    @classmethod
    def _new_from_subunit(cls, value: int) -> Self:
        if isinstance(value, int):
            conversion = value / 10**cls.subunit_size
            return cls(conversion)
        raise TypeError(f"Invalid type for subunit value: {type(value)}")

    def formatted(self) -> str:
        sep = " " if self.symbol_space else ""
        if self.symbol_begining:
            return f"{self.symbol}{sep}{self.__str__()}"
        else:
            return f"{self.__str__()}{sep}{self.symbol}"

    def _is_same_currency(self, other: Any) -> bool:
        return self.__class__.__mro__ == other.__class__.__mro__

    @classmethod
    def _is_currency(cls, other: Any) -> bool:
        return all(
            x in other.__class__.__dict__.keys() for x in cls.__dict__.keys()
        )
