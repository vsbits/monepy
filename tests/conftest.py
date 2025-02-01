import pytest
from currency.base import _Currency


@pytest.fixture()
def generic_currency():
    class Generic(_Currency):
        symbol = "GEN"
        symbol_space = True
        symbol_begining = True
        thousand_sep = " "
        subunit_size = 1
        subunit_sep = "."

    yield Generic
