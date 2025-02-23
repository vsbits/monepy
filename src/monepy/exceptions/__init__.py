class ConvertionError(Exception):
    """Base error for convertion operations"""
    pass

class ConvertionRatesNotDefined(ConvertionError):
    """Convertion rates where not configured for the selected class"""

class ConvertionRateNotFound(ConvertionError, KeyError):
    """Conversion rates are configured, but the desired currency was not
    found"""
