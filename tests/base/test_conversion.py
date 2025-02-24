class TestConversionMethod:
    def test_from_conversion(self, generic_currency, other_generic_currency):
        v1 = other_generic_currency(1)
        other_generic_currency.set_rates({"Generic": 2})
        result = generic_currency.from_conversion(v1)
        assert result == generic_currency(2)
