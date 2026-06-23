contact_book={
    "Police":100,
    "Fire":101,
    "Ambulance":102,
    "Home":7385971107,
    "His":6987652390,
    "Hers":8990356283
}

def display_contact():
    return contact_book

def add_contact():
    name=input("Enter your name: ")
    phone=int(input("Enter your phone number: "))
    contact_book.update({name:phone})
    return contact_book

def update_contact():
    name=input("Enter the name to be updated: ")
    phone=int(input("Enter the phone number: "))
    contact_book.update({name:phone})
    return contact_book

def remove_contact():
    name=input("Enter the name to be removed: ")
    del contact_book[name]
    return contact_book

def search_contact():
    name=input("Enter the name: ")
    x=contact_book.get(name)
    return x

while True:
    choice=int(input('''1=display,2=add contact,3=update contact,4=remove contact,5=search contact,6=exit
    Enter your choice: '''))
    if choice==1:
        print(display_contact())
    elif choice==2:
        print(add_contact())
    elif choice==3:
        print(update_contact())
    elif choice==4:
        print(remove_contact())
    elif choice==5:
        print(search_contact())
    elif choice==6:
        break
    else:
        print("Invalid choice")
