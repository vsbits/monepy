import pytest


class TestOperators:
    @pytest.mark.parametrize(
        ["value", "expected"],
        [
            [1, 1],
            [-1, 1],
            [0.1, 0.1],
            [-0.1, 0.1],
        ],
    )
    def test_abs(self, generic_currency, value, expected):
        v = generic_currency(value)
        assert abs(v) == expected

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

    def test_eq_numeric(self, generic_currency):
        v = generic_currency(1)
        assert (v == 1) is False

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

    def test_greater_numeric(self, generic_currency):
        v = generic_currency(1)
        with pytest.raises(NotImplementedError):
            _ = v > 1

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

    def test_ge_numeric(self, generic_currency):
        v = generic_currency(1)
        with pytest.raises(NotImplementedError):
            _ = v >= 1

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


    def test_lesser_numeric(self, generic_currency):
        v = generic_currency(1)
        with pytest.raises(NotImplementedError):
            _ = v < 1

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

    def test_le_numeric(self, generic_currency):
        v = generic_currency(1)
        with pytest.raises(NotImplementedError):
            _ = v < 1

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"], [[1, 2, 3], [1.5, 1.5, 3], [0, 0, 0]]
    )
    def test_sum(self, generic_currency, value1, value2, expected):
        result = generic_currency(value1) + generic_currency(value2)
        assert result == generic_currency(expected)

    def test_sum_zero(self, generic_currency):
        v = generic_currency(1)
        result = v + 0
        assert result == v

    @pytest.mark.parametrize("to_sum", [1, 1.0, "1"])
    def test_sum_wrong_type(self, generic_currency, to_sum):
        v = generic_currency(1)
        with pytest.raises(TypeError):
            _ = v + to_sum

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [[100, 1, 99], [100, 200, -100], [100, 0.1, 99.9]],
    )
    def test_sub(self, generic_currency, value1, value2, expected):
        result = generic_currency(value1) - generic_currency(value2)
        assert result == generic_currency(expected)

    @pytest.mark.parametrize("to_sub", [1, 1.0, "1"])
    def test_sub_wrong_type(self, generic_currency, to_sub):
        v = generic_currency(1)
        with pytest.raises(TypeError):
            _ = v - to_sub

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"], [[1, 2, 2], [1, 2.0, 2], [1, -1, -1]]
    )
    def test_mul(self, generic_currency, value1, value2, expected):
        v = generic_currency(value1)
        result = v * value2
        assert result == generic_currency(expected)

    def test_mul_wrong_type(self, generic_currency):
        v = generic_currency(1)
        with pytest.raises(TypeError):
            _ = v * "1"
        with pytest.raises(TypeError):
            _ = v * v

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, 1],
            [1, 2.0, 0.5],
            [1, 3, 0.3],
            [1, -2, -0.5],
        ],
    )
    def test_truediv(self, generic_currency, value1, value2, expected):
        v = generic_currency(value1)
        result = v / value2
        assert result == generic_currency(expected)

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1, 1, 1.0],
            [10, 5, 2.0],
            [1, 2, 0.5],
            [1, -1, -1.0],
        ],
    )
    def test_truediv_class(self, generic_currency, value1, value2, expected):
        v = generic_currency(value1)
        div = generic_currency(value2)

        result = v / div
        assert result == expected

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [10, 5, 2],
            [1.5, 1, 1],
            [-2, 0.5, -4],
        ],
    )
    def test_floordiv_same_currency(
        self,
        generic_currency,
        value1,
        value2,
        expected
    ):
        v1 = generic_currency(value1)
        v2 = generic_currency(value2)
        result = v1 // v2
        assert result == expected

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [10, 5, 2],
            [1.5, 1, 1.5],
            [-2, 0.5, -4],
        ]
    )
    def test_floordiv(self, generic_currency, value1, value2, expected):
        v1 = generic_currency(value1)
        result = v1 // value2
        assert result == generic_currency(expected)

    def test_floordiv_diff_curency(
        self, generic_currency, other_generic_currency
    ):
        with pytest.raises(NotImplementedError):
            _ = generic_currency(1) // other_generic_currency(1)

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [1.1, 2, 0.1],
            [1, 2.0, 0],
            [1.9, 4, 0.3],
            [0.3, -2, -0.1],
            [-1.1, -2, -0.1],
            [-1.1, 2, 0.1],
        ],
    )
    def test_mod(self, generic_currency, value1, value2, expected):
        v = generic_currency(value1)
        result = v % value2
        assert result == generic_currency(expected)

    @pytest.mark.parametrize(
        ["value1", "value2", "expected"],
        [
            [10, 5, 0],
            [1.5, 1, 0.5],
            [-2.3, 0.5, 0.3],
            [0.3, -0.2, -0.1],
            [-1.1, -0.2, -0.1],
        ],
    )
    def test_mod_class(
        self, generic_currency, value1, value2, expected
    ):
        v1 = generic_currency(value1)
        v2 = generic_currency(value2)
        result = v1 % v2
        assert result == generic_currency(expected)

    def test_mod_diff_curency(
        self, generic_currency, other_generic_currency
    ):
        with pytest.raises(NotImplementedError):
            _ = generic_currency(1) % other_generic_currency(1)


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
