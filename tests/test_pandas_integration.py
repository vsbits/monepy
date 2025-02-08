import pandas as pd


class TestPandasSeries:
    def test_series_from_list(self, generic_currency):
        values = [generic_currency(x) for x in range(10)]
        _ = pd.Series(values)

    def test_series_convert_to_currency(self, generic_currency):
        s = pd.Series(range(10))
        _ = s.apply(generic_currency)

    def test_series_sum(self, generic_currency):
        values = [generic_currency(x) for x in [1, 1]]
        s = pd.Series(values)
        total = s.sum()
        assert isinstance(total, generic_currency)
        assert total == 2
