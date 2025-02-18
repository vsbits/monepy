import pytest


class TestCurrency:
    @pytest.mark.parametrize(
        ["value", "expected"], [[1, 1], [1.0, 1], [-0.1, -0.1]]
    )
    def test_init(self, generic_currency, value, expected):
        v = generic_currency(value)
        assert v == expected

    @pytest.mark.parametrize("value", ["1", 0.33])
    def test_init_exception(self, generic_currency, value):
        with pytest.raises(ValueError):
            _ = generic_currency(value)

    @pytest.mark.parametrize("value", [1, -1])
    def test_new_from_subunit(self, generic_currency, value):
        v = generic_currency._new_from_subunit(value)
        assert v._value == value

    @pytest.mark.parametrize("value", ["1", 1.1111])
    def test_exception_new_from_subunit(self, generic_currency, value):
        with pytest.raises(TypeError):
            _ = generic_currency._new_from_subunit(value)

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, True],
            [-1, 1, False],
        ],
    )
    def test_hash_dif_value(self, generic_currency, value1, value2, expected):
        v1 = generic_currency(value1)
        v2 = generic_currency(value2)
        assert (hash(v1) == hash(v2)) is expected

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, False],
            [-1, 1, False],
        ],
    )
    def test_hash_dif_currency(
        self,
        generic_currency,
        other_generic_currency,
        value1,
        value2,
        expected,
    ):
        v1 = generic_currency(value1)
        v2 = other_generic_currency(value2)
        assert (hash(v1) == hash(v2)) is expected


class TestMethods:
    def test_sum(self, generic_currency):
        values = [generic_currency(x) for x in (1, 2, 3)]
        result = generic_currency.sum(values)
        assert isinstance(result, generic_currency)
        assert result == 6

    def test_sum_empty_list(self, generic_currency):
        values = []
        result = generic_currency.sum(values)
        assert isinstance(result, generic_currency)
        assert result == 0

    def test_sum_wrong_currency(
        self, generic_currency, other_generic_currency
    ):
        values = [generic_currency(x) for x in (1, 2, 3)]
        with pytest.raises(ValueError):
            _ = other_generic_currency(values)
