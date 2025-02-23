from .base import _Currency


class BRL(_Currency):
    """Class to represent Brazilian real"""

    _symbol = "R$"
    _symbol_space = True
    _symbol_begining = True
    _thousand_sep = "."
    _subunit_size = 2
    _subunit_sep = ","


class EUR(_Currency):
    """Class to represent Euro"""

    _symbol = "€"
    _symbol_space = True
    _symbol_begining = False
    _thousand_sep = " "
    _subunit_size = 2
    _subunit_sep = ","


class USD(_Currency):
    """Class to represent US dollar"""

    _symbol = "$"
    _symbol_space = False
    _symbol_begining = True
    _thousand_sep = ","
    _subunit_size = 2
    _subunit_sep = "."


class JPY(_Currency):
    """Class to represent Japanese yen"""

    _symbol = "¥"
    _symbol_space = False
    _symbol_begining = True
    _thousand_sep = ","
    _subunit_size = 0
    _subunit_sep = None


class GBP(_Currency):
    """Class to represent UK Sterling"""
    _symbol = "£"
    _symbol_space = False
    _symbol_begining = True
    _thousand_sep = ","
    _subunit_size = 2
    _subunit_sep = "."
