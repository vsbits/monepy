from currency.utils import sum_
from currency.currencies import BRL, USD
import pytest


class TestSum:
    def test_sum(self):
        values = [BRL(100), BRL(200), BRL(300)]
        total = sum_(values)
        assert total.__class__ == BRL
        assert total.value == 600


    def test_wrong_types_sum(self):
        values = [BRL(100), BRL(200), USD(300)]
        with pytest.raises(ValueError):
            _ = sum_(values)


    def test_empty_sum(self):
        values = []
        with pytest.raises(ValueError):
            _ = sum_(values)
