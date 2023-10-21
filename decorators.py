from custom_exceptions import (
    MissingName, MissingPhoneNumber, NameCannotBeNumeric, NoData, PhoneNotFound, IncorrectPhoneFormat,
    NoDataFound, DuplicateEntry
)


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Not found."
        except IndexError:
            return "Missing argument."
        except NoData:
            return "No data entered."
        except MissingName:
            return "Missing the contact's name."
        except MissingPhoneNumber:
            return "Missing the phone number."
        except IncorrectPhoneFormat:
            return "Please, enter a valid phone format (10 digits)."
        except NoDataFound:
            return "No data found."
        except DuplicateEntry:
            return "A duplicate entry was found."
        except NameCannotBeNumeric:
            return "The name cannot be numeric."
        except PhoneNotFound:
            return "Phone number or contact not found."
        except Exception as e:
            return str(e)
    return inner
