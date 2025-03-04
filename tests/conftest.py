import pytest
from monepy.currency.base import _Currency


@pytest.fixture(scope="function")
def generic_currency():
    class Generic(_Currency):
        _symbol = "GEN"
        _symbol_space = True
        _symbol_begining = True
        _thousand_sep = " "
        _subunit_size = 1
        _subunit_sep = "."

    yield Generic


@pytest.fixture(scope="function")
def other_generic_currency():
    class OtherGeneric(_Currency):
        _symbol = "OTH"
        _symbol_space = True
        _symbol_begining = False
        _thousand_sep = " "
        _subunit_size = 2
        _subunit_sep = ","

    yield OtherGeneric

@pytest.fixture(scope="function")
def another_generic_currency():
    class AnotherGeneric(_Currency):
        _symbol = "ANO"
        _symbol_space = True
        _symbol_begining = False
        _thousand_sep = " "
        _subunit_size = 2
        _subunit_sep = ","

    yield AnotherGeneric
