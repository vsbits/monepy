from .base import _Currency


class BRL(_Currency):
    symbol = "R$"
    symbol_space = True
    symbol_begining = True
    thousand_sep = "."
    subunit_size = 2
    subunit_sep = ","


class EUR(_Currency):
    symbol = "€"
    symbol_space = True
    symbol_begining = False
    thousand_sep = " "
    subunit_size = 2
    subunit_sep = ","


class USD(_Currency):
    symbol = "$"
    symbol_space = False
    symbol_begining = True
    thousand_sep = ","
    subunit_size = 2
    subunit_sep = "."
