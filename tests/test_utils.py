from monepy.utils import _sum, _mean, convert
from monepy.exceptions import ConversionRateNotFound, ConversionRatesNotDefined
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
        assert total == generic_currency(20)

    def test_wrong_types_mean(self, generic_currency, other_generic_currency):
        values = [generic_currency(1), other_generic_currency(1)]
        with pytest.raises(ValueError):
            _ = _mean(values)

    def test_empty_mean(self):
        values = []
        with pytest.raises(ValueError):
            _ = _mean(values)


class TestConversion:
    def test_convert(self, generic_currency, other_generic_currency):
        v1 = generic_currency(1)
        other_generic_currency.set_rates({"Generic": 2})
        result = convert(v1, other_generic_currency)
        assert result == other_generic_currency(0.5)

    def test_convert_from(self, generic_currency, other_generic_currency):
        v1 = generic_currency(1)
        generic_currency.set_rates({"OtherGeneric": 2})
        result = convert(v1, other_generic_currency)
        assert result == other_generic_currency(2)
    
    def test_convert_using_base(
        self,
        generic_currency,
        other_generic_currency,
        another_generic_currency
    ):
        v1 = generic_currency(1)
        another_generic_currency.set_rates(
            {
                "Generic": 0.5,
                "OtherGeneric": 2
            }
        )
        result = convert(
            v1,
            other_generic_currency,
            base=another_generic_currency
        )
        assert result == other_generic_currency(4)

    def test_undefined_conversion(
        self, generic_currency, other_generic_currency
    ):
        v1 = generic_currency(1)
        with pytest.raises(ConversionRatesNotDefined):
            _ = convert(v1, other_generic_currency)

    def test_currency_conversion_not_found(
        self, generic_currency, other_generic_currency
    ):
        v1 = generic_currency(1)
        other_generic_currency.set_rates({})
        with pytest.raises(ConversionRateNotFound):
            _ = convert(v1, other_generic_currency)
