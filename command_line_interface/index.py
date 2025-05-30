def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts: dict[str, str]):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts: dict[str, str]):
    if not args:
        return "Invalid input data"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."
    
def show_all(contacts: dict[str, str]):
    if not contacts:
        return "Contacts are empty."
    contactsList = ""

    for key, value in contacts.items():
        contactsList += f"{key} => {value}\n"

    return contactsList

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break
                case "hello":
                    print("How can I help you?")
                case "add":
                    print(add_contact(args, contacts))
                case "change":
                    print(change_contact(args, contacts))
                case "phone":
                    print(show_phone(args, contacts))
                case "all":
                    print(show_all(contacts))    
                case _:
                    print(ERROR_MESSAGE)
        except ValueError as e:
            print(e)

# constants
EXIT = "exit"
CLOSE = "close" 
ERROR_MESSAGE = "Invalid command."   

if __name__ == '__main__':
    main()
