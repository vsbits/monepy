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


@pytest.fixture()
def other_generic_currency():
    class OtherGeneric(_Currency):
        symbol = "OTH"
        symbol_space = True
        symbol_begining = False
        thousand_sep = " "
        subunit_size = 2
        subunit_sep = ","

    yield OtherGeneric
