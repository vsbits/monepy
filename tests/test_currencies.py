from currency.base import _Currency
from currency.currencies import BRL, EUR, USD
import pytest


class TestBRL:
    def test_mul(self):
        v = BRL(100)
        assert (v * 2).value == 200
        assert (v * 2.0).value == 200
        assert (v * -1.0).value == -100

    @pytest.mark.parametrize(
        ["value", "result"],
        [
            [1, 100],
            [2.0, 50],
            [3, 33],
            [-2, -50],
        ]
    )
    def test_truediv(self, value, result):
        v = BRL(100)
        assert (v / value).value == result

    @pytest.mark.parametrize(
        ["value", "result"],
        [
            [100, 1.0],
            [50, 2.0],
            [200, 0.5],
            [-100, -1.0],
        ]
    )
    def test_truediv_class(self, value, result):
        v = BRL(100)
        div = BRL(value)
        assert v / div == result

    def test_mul_wrong_type(self):
        v = BRL(1)
        with pytest.raises(TypeError):
            _ = v * v  # type: ignore
        with pytest.raises(TypeError):
            _ = v * "1"  # type: ignore


class TestDiffCurrencies:
    def test_sum(self):
        with pytest.raises(TypeError):
            _ = EUR(1) + _Currency(1)  # type: ignore

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
        [USD, "<USD 1,000.00>"]
    ]
)
def test_repr(cls, result):
    assert cls(100000).__repr__() == result


class TestFormat:
    @pytest.mark.parametrize(
        ["cls", "result"],
        [
            [BRL, "R$ 1.000,00"],
            [EUR, "1 000,00 €"],
            [USD, "$1,000.00"]
        ]
    )
    def test_format_negative(self, cls, result):
        assert cls(100000).formatted() == result

    @pytest.mark.parametrize(
        ["cls", "result"],
        [
            [BRL, "R$ -1.000,00"],
            [EUR, "-1 000,00 €"],
            [USD, "$-1,000.00"]
        ]
    )
    def test_format(self, cls, result):
        assert cls(-100000).formatted() == result
