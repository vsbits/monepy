from monepy import BRL, EUR, USD, JPY
import pytest


class TestDiffCurrencies:
    def test_sum(self, generic_currency):
        with pytest.raises(TypeError):
            _ = EUR(1) + generic_currency(1)  # type: ignore

    def test_sub(self):
        with pytest.raises(TypeError):
            _ = EUR(1) - BRL(1)  # type: ignore

    def test_truediv(self):
        with pytest.raises(TypeError):
            _ = EUR(1) / USD(1)  # type: ignore


@pytest.mark.parametrize(
    ["cls", "result"],
    [
        [BRL, "<BRL 1.000,00>"],
        [EUR, "<EUR 1 000,00>"],
        [USD, "<USD 1,000.00>"],
        [JPY, "<JPY 1,000>"]
    ]
)
def test_repr(cls, result):
    assert cls(1000).__repr__() == result


class TestFormat:
    @pytest.mark.parametrize(
        ["cls", "result"],
        [
            [BRL, "R$ 1.000,00"],
            [EUR, "1 000,00 €"],
            [USD, "$1,000.00"],
            [JPY, "¥1,000"]
        ]
    )
    def test_format_negative(self, cls, result):
        assert cls(1000).formatted() == result

    @pytest.mark.parametrize(
        ["cls", "result"],
        [
            [BRL, "R$ -1.000,00"],
            [EUR, "-1 000,00 €"],
            [USD, "$-1,000.00"],
            [JPY, "¥-1,000"]
        ]
    )
    def test_format(self, cls, result):
        assert cls(-1000).formatted() == result
