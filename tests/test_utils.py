from monepy.utils import _sum, _mean
import pytest


class TestSum:
    def test_sum(self, generic_currency):
        values = [
            generic_currency(1),
            generic_currency(1.5),
            generic_currency(0.5),
        ]
        total = _sum(values)
        assert total.__class__ == generic_currency
        assert total._value == 30

    def test_wrong_types_sum(self, generic_currency, other_generic_currency):
        values = [generic_currency(1), other_generic_currency(1)]
        with pytest.raises(ValueError):
            _ = _sum(values)

    def test_empty_sum(self):
        values = []
        with pytest.raises(ValueError):
            _ = _sum(values)


class TestMean:
    def test_mean(self, generic_currency):
        values = [
            generic_currency(10),
            generic_currency(20),
            generic_currency(30),
        ]
        total = _mean(values)
        assert total.__class__ == generic_currency
        assert total == 20

    def test_wrong_types_mean(self, generic_currency, other_generic_currency):
        values = [generic_currency(1), other_generic_currency(1)]
        with pytest.raises(ValueError):
            _ = _mean(values)

    def test_empty_mean(self):
        values = []
        with pytest.raises(ValueError):
            _ = _mean(values)
