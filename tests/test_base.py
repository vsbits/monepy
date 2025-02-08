import pytest


class TestCurrency:
    @pytest.mark.parametrize(
        ["value", "expected"], [[1, 1], [1.0, 1], [-0.1, -0.1]]
    )
    def test_init(self, generic_currency, value, expected):
        v = generic_currency(value)
        assert v.value == expected * 10**generic_currency.subunit_size

    @pytest.mark.parametrize("value", ["1", 0.33])
    def test_init_exception(self, generic_currency, value):
        with pytest.raises(ValueError):
            _ = generic_currency(value)

    @pytest.mark.parametrize("value", [1, -1])
    def test_new_from_subunit(self, generic_currency, value):
        v = generic_currency._new_from_subunit(value)
        assert v.value == value

    @pytest.mark.parametrize("value", ["1", 1.1111])
    def test_exception_new_from_subunit(self, generic_currency, value):
        with pytest.raises(TypeError):
            _ = generic_currency._new_from_subunit(value)


class TestOperators:
    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, True],
            [-1, -1, True],
            [1, -1, False],
            [1, 2, False],
        ],
    )
    def test_eq(self, generic_currency, value1, value2, expected):
        v1 = generic_currency(value1)
        v2 = generic_currency(value2)
        assert (v1 == v2) is expected
        assert (v1 != v2) is not expected

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, True],
            [1, 1.0, True],
            [1.1, 1, False],
            [1, 2, False],
            [1, -1, False],
            [1, "abc", False],
            [1, "1", False],
        ],
    )
    def test_eq_numeric(self, generic_currency, value1, value2, expected):
        v = generic_currency(value1)
        assert (v == value2) is expected
        assert (v != value2) is not expected

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, False],
            [-1, -1, False],
            [1, -1, True],
            [1, 2, False],
            [1, 1.1, False],
            [1.2, 1.1, True],
        ],
    )
    def test_greater(self, value1, value2, expected, generic_currency):
        v1 = generic_currency(value1)
        v2 = generic_currency(value2)
        assert (v1 > v2) is expected

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, False],
            [-1, -1, False],
            [1, -1, True],
            [1, 2, False],
            [1, 1.1, False],
            [1.2, 1.1, True],
        ],
    )
    def test_greater_numeric(self, generic_currency, value1, value2, expected):
        v = generic_currency(value1)
        assert (v > value2) is expected

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, True],
            [-1, -1, True],
            [1, -1, True],
            [1, 2, False],
            [1, 1.1, False],
            [1.2, 1.1, True],
        ],
    )
    def test_ge(self, value1, value2, expected, generic_currency):
        v1 = generic_currency(value1)
        v2 = generic_currency(value2)
        assert (v1 >= v2) is expected

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, True],
            [-1, -1, True],
            [1, -1, True],
            [1, 2, False],
            [1, 1.1, False],
            [1.2, 1.1, True],
        ],
    )
    def test_ge_numeric(self, generic_currency, value1, value2, expected):
        v = generic_currency(value1)
        assert (v >= value2) is expected

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, False],
            [-1, -1, False],
            [1, -1, False],
            [1, 2, True],
            [1, 1.1, True],
            [1.2, 1.1, False],
        ],
    )
    def test_lesser(self, value1, value2, expected, generic_currency):
        v1 = generic_currency(value1)
        v2 = generic_currency(value2)
        assert (v1 < v2) is expected

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, False],
            [-1, -1, False],
            [1, -1, False],
            [1, 2, True],
            [1, 1.1, True],
            [1.2, 1.1, False],
        ],
    )
    def test_lesser_numeric(self, generic_currency, value1, value2, expected):
        v = generic_currency(value1)
        assert (v < value2) is expected

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, True],
            [-1, -1, True],
            [1, -1, False],
            [1, 2, True],
            [1, 1.1, True],
            [1.2, 1.1, False],
        ],
    )
    def test_le(self, value1, value2, expected, generic_currency):
        v1 = generic_currency(value1)
        v2 = generic_currency(value2)
        assert (v1 <= v2) is expected

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, True],
            [-1, -1, True],
            [1, -1, False],
            [1, 2, True],
            [1, 1.1, True],
            [1.2, 1.1, False],
        ],
    )
    def test_le_numeric(self, generic_currency, value1, value2, expected):
        v = generic_currency(value1)
        assert (v <= value2) is expected

    @pytest.mark.parametrize(
        ["value1", "value2", "result"], [[1, 2, 3], [1.5, 1.5, 3], [0, 0, 0]]
    )
    def test_sum(self, generic_currency, value1, value2, result):
        total = generic_currency(value1) + generic_currency(value2)
        print(generic_currency(value2).value)
        assert total.value == result * 10**generic_currency.subunit_size

    @pytest.mark.parametrize("to_sum", [1, 1.0, "1"])
    def test_sum_wrong_type(self, generic_currency, to_sum):
        v = generic_currency(1)
        with pytest.raises(TypeError):
            _ = v + to_sum

    @pytest.mark.parametrize(
        ["value1", "value2", "result"],
        [[100, 1, 99], [100, 200, -100], [100, 0.1, 99.9]],
    )
    def test_sub(self, generic_currency, value1, value2, result):
        total = generic_currency(value1) - generic_currency(value2)
        assert total.value == result * 10**generic_currency.subunit_size

    @pytest.mark.parametrize("to_sub", [1, 1.0, "1"])
    def test_sub_wrong_type(self, generic_currency, to_sub):
        v = generic_currency(1)
        with pytest.raises(TypeError):
            _ = v - to_sub

    @pytest.mark.parametrize(
        ["value1", "value2", "result"], [[1, 2, 2], [1, 2.0, 2], [1, -1, -1]]
    )
    def test_mul(self, generic_currency, value1, value2, result):
        v = generic_currency(value1)
        total = v * value2
        assert total.value == result * 10**generic_currency.subunit_size

    def test_mul_wrong_type(self, generic_currency):
        v = generic_currency(1)
        with pytest.raises(TypeError):
            _ = v * "1"
        with pytest.raises(TypeError):
            _ = v * v

    @pytest.mark.parametrize(
        ["value1", "value2", "result"],
        [
            [1, 1, 1],
            [1, 2.0, 0.5],
            [1, 3, 0.3],
            [1, -2, -0.5],
        ],
    )
    def test_truediv(self, generic_currency, value1, value2, result):
        v = generic_currency(value1)
        value = (v / value2).value
        assert value == int(result * 10**generic_currency.subunit_size)

    @pytest.mark.parametrize(
        ["value1", "value2", "result"],
        [
            [1, 1, 1.0],
            [10, 5, 2.0],
            [1, 2, 0.5],
            [1, -1, -1.0],
        ],
    )
    def test_truediv_class(self, generic_currency, value1, value2, result):
        v = generic_currency(value1)
        div = generic_currency(value2)

        value = v / div
        assert value == result


class TestOperatorsDifferentCurrencies:
    def test_eq(self, generic_currency, other_generic_currency):
        with pytest.raises(NotImplementedError):
            _ = generic_currency(1) == other_generic_currency(1)

    def test_ne(self, generic_currency, other_generic_currency):
        with pytest.raises(NotImplementedError):
            _ = generic_currency(1) != other_generic_currency(1)

    def test_gt(self, generic_currency, other_generic_currency):
        with pytest.raises(NotImplementedError):
            _ = generic_currency(1) > other_generic_currency(1)

    def test_ge(self, generic_currency, other_generic_currency):
        with pytest.raises(NotImplementedError):
            _ = generic_currency(1) >= other_generic_currency(1)

    def test_lt(self, generic_currency, other_generic_currency):
        with pytest.raises(NotImplementedError):
            _ = generic_currency(1) < other_generic_currency(1)

    def test_le(self, generic_currency, other_generic_currency):
        with pytest.raises(NotImplementedError):
            _ = generic_currency(1) <= other_generic_currency(1)
