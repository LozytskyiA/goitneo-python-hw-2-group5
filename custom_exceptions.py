class NoData(Exception):
    """Raised when no data is entered."""
    pass


class MissingName(Exception):
    """Exception raised when the name is missing."""
    pass


class NameCannotBeNumeric(Exception):
    """Exception raised when the provided name is numeric."""
    pass


class MissingPhoneNumber(Exception):
    """Exception raised when the phone number is missing."""
    pass


class PhoneNotFound(Exception):
    """Raised when the entered phone number is not found."""
    pass


class IncorrectPhoneFormat(Exception):
    """Raised when the phone format is incorrect."""
    pass


class NoDataFound(Exception):
    """Raised when no data is found for the provided input."""
    pass


class DuplicateEntry(Exception):
    """Raised when a duplicate entry is found."""
    pass
