import pytest
from currency.base import _Currency


class TestCurrency:
    def test_init(self):
        v = _Currency(1)
        assert v.value == 1

    @pytest.mark.parametrize(
        ["value", "result"],
        [
            [1, 101],
            [2, 102],
            [-10, 90]
        ]
    )
    def test_sum(self, value, result):
        total = _Currency(100) + _Currency(value)
        assert total.value == result

    @pytest.mark.parametrize("to_sum", [1, 1.0, "1"])
    def test_sum_wrong_type(self, to_sum):
        v = _Currency(1)
        with pytest.raises(TypeError):
            _ = v + to_sum

    @pytest.mark.parametrize(
        ["value", "result"],
        [
            [1, 99],
            [200, -100],
            [50, 50]
        ]
    )
    def test_sub(self, value, result):
        total = _Currency(100) - _Currency(value)
        assert total.value == result

    @pytest.mark.parametrize("to_sub", [1, 1.0, "1"])
    def test_sub_wrong_type(self, to_sub):
        v = _Currency(1)
        with pytest.raises(TypeError):
            _ = v - to_sub
