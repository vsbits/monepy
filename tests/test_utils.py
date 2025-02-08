from currency.utils import sum_
import pytest


class TestSum:
    def test_sum(self, generic_currency):
        values = [
            generic_currency(1), generic_currency(1.5), generic_currency(0.5)
        ]
        total = sum_(values)
        assert total.__class__ == generic_currency
        assert total.value == 30

    def test_wrong_types_sum(self, generic_currency, other_generic_currency):
        values = [generic_currency(1), other_generic_currency(1)]
        with pytest.raises(ValueError):
            _ = sum_(values)

    def test_empty_sum(self):
        values = []
        with pytest.raises(ValueError):
            _ = sum_(values)
