import pandas as pd


class TestPandasSeries:
    def test_series_from_list(self, generic_currency):
        values = [generic_currency(x) for x in range(10)]
        _ = pd.Series(values)

    def test_series_convert_to_currency(self, generic_currency):
        s = pd.Series(range(10))
        _ = s.map(generic_currency)

    def test_series_convert_with_NA(self, generic_currency):
        s = pd.Series(range(10))
        s[2] = pd.NA
        _ = s.map(generic_currency, na_action="ignore")
