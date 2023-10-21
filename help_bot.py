from decorators import input_error
from custom_exceptions import (
    MissingName, MissingPhoneNumber, NameCannotBeNumeric, NoData, PhoneNotFound, IncorrectPhoneFormat,
    NoDataFound, DuplicateEntry
)


def parse_input(user_input):
    if not user_input.strip():
        return None,
    command, *args = user_input.split()
    command = command.lower().strip()
    return command, args


@input_error
def add_contact(args, contacts):
    if len(args) == 0:
        raise MissingName()

    if len(args) == 1:
        name = args[0]
        if name.isdigit():
            raise NameCannotBeNumeric()
        else:
            raise MissingPhoneNumber()

    name, phone = args

    if name.isdigit():
        raise NameCannotBeNumeric()

    if not phone.isdigit() or len(phone) != 10:
        raise IncorrectPhoneFormat()

    if name in contacts:
        raise DuplicateEntry()

    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if not phone.isdigit() or len(phone) != 10:
        raise IncorrectPhoneFormat()

    if name not in contacts:
        raise PhoneNotFound
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    if not args:
        raise NoData
    name = args[0]
    if name not in contacts:
        raise PhoneNotFound
    return contacts[name]


@input_error
def show_all(contacts):
    if not contacts:
        raise NoDataFound
    return '\n'.join(f'{name}: {phone}' for name, phone in contacts.items())


def show_help():
    print("\nInstructions:")
    print('1. To add a contact, type: add "name" "phone number"')
    print('2. To change a contact\'s phone number, type: change "name" "new phone number"')


def main():
    print("Welcome to the assistant bot! Type 'help' to see available commands.")
    contacts = {}
    while True:
        try:
            user_input = input("Enter a command: ")
            if user_input.strip() == "":
                print("You didn't enter anything.")
                continue

            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "help":
                show_help()
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                print("Invalid command.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
