from typing import Self, Union, overload


class _Currency:
    """Class to reprensent a currency.
    Should not be direcly instanciated."""
    value: int
    """Stored value in the smallest unit for the selected currency.
    e.g.: cents for USD"""
    symbol: str
    symbol_space: bool
    symbol_begining: bool
    thousand_sep: str
    subunit_size: int
    subunit_sep: str

    def __init__(self, value: int):
        self.value = value

    def __str__(self) -> str:
        chars = str(abs(self.value)).zfill(self.subunit_size + 1)
        rev = [char for char in chars]
        rev.reverse()
        value_as_str = ""
        for i, n in enumerate(rev, 0):

            if i == self.subunit_size:
                value_as_str = self.subunit_sep + value_as_str

            elif (i - self.subunit_size) % 3 == 0:
                value_as_str = self.thousand_sep + value_as_str

            value_as_str = n + value_as_str

        if self.value < 0:
            value_as_str = "-" + value_as_str
        return value_as_str

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.__str__()}>"

    def __add__(self, other: Self) -> Self:
        if other.__class__ == self.__class__:
            return self.__class__(self.value + other.value)
        raise TypeError(
            "Can't add objects of type "
            f"{self.__class__} and {other.__class__}"
        )

    def __sub__(self, other: Self) -> Self:
        if other.__class__ == self.__class__:
            return self.__class__(self.value - other.value)
        raise TypeError(
            "Can't subtract objects of type "
            f"{self.__class__} and {other.__class__}"
        )

    def __mul__(self, other: Union[int, float]) -> Self:
        if other.__class__ in (int, float):
            return self.__class__(int(self.value * other))
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
        if isinstance(other, self.__class__) and (
            other.__class__ == self.__class__
        ):
            return self.value / other.value
        elif isinstance(other, float) or isinstance(other, int):
            return self.__class__(int(self.value / other))
        raise TypeError(
            "Can't divide objects of type "
            f"{self.__class__} by {other.__class__}"
        )

    def formatted(self) -> str:
        sep = " " if self.symbol_space else ""
        if self.symbol_begining:
            return f"{self.symbol}{sep}{self.__str__()}"
        else:
            return f"{self.__str__()}{sep}{self.symbol}"
