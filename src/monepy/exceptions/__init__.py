class ConversionError(Exception):
    """Base error for conversion operations"""
    pass

class ConversionRatesNotDefined(ConversionError):
    """Conversion rates where not configured for the selected class"""

class ConversionRateNotFound(ConversionError, KeyError):
    """Conversion rates are configured, but the desired currency was not
    found"""
