from bot.AddressBook import AddressBook

def main_cli():
    addressBook = AddressBook()
    while True:
        command, *args = input(">>> ").strip().split(' ')
        if command == 'add':
            name, phone = args
            addressBook.update({name: phone})
            print('User added')
        elif command == 'all':
            print(addressBook)
        elif command in ['bye', 'exit']:
            print("Good bye!")
            break

if __name__ == '__main__':
    main_cli()