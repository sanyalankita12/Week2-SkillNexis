# ---------- CRUD Operations on a List ----------

cities = []

def display_cities():
    if cities:
        print("Cities:", cities)
    else:
        print("No cities available.")

def add_city():
    city = input("Enter city name to add: ")
    cities.append(city)
    print(f"{city} added successfully.")

def remove_city():
    city = input("Enter city name to remove: ")
    if city in cities:
        cities.remove(city)
        print(f"{city} removed successfully.")
    else:
        print("City not found.")

def update_city():
    old_city = input("Enter city to update: ")
    if old_city in cities:
        new_city = input("Enter new city name: ")
        index = cities.index(old_city)
        cities[index] = new_city
        print("City updated successfully.")
    else:
        print("City not found.")

while True:
    print("""
    1. Display Cities
    2. Add City
    3. Remove City
    4. Update City
    5. Exit
    """)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_cities()

    elif choice == 2:
        add_city()

    elif choice == 3:
        remove_city()

    elif choice == 4:
        update_city()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")