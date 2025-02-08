from .base import _Currency


class BRL(_Currency):
    """Class to represent Brazilian real"""

    symbol = "R$"
    symbol_space = True
    symbol_begining = True
    thousand_sep = "."
    subunit_size = 2
    subunit_sep = ","


class EUR(_Currency):
    """Class to represent Euro"""

    symbol = "€"
    symbol_space = True
    symbol_begining = False
    thousand_sep = " "
    subunit_size = 2
    subunit_sep = ","


class USD(_Currency):
    """Class to represent US dollar"""

    symbol = "$"
    symbol_space = False
    symbol_begining = True
    thousand_sep = ","
    subunit_size = 2
    subunit_sep = "."


class JPY(_Currency):
    """Class to represent Japanese yen"""

    symbol = "¥"
    symbol_space = False
    symbol_begining = True
    thousand_sep = ","
    subunit_size = 0
    subunit_sep = None
