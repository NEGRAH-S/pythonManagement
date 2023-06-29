#fileCode2
# Import required modules
import csv

# Constants
DATA_FILE = 'grocery_data.csv'  # CSV file to store grocery data

# Function to display the main menu
def display_menu():
    print("\n*** Grocery Management System Menu ***")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Remove Item")
    print("4. Search Item")
    print("5. Display All Items")
    print("6. Exit")

# Function to add an item to the grocery list
def add_item():
    # Get item details from user
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))

    # Append item to CSV file
    with open(DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, price, quantity])
    print("Item added successfully!")

# Function to update an item in the grocery list
def update_item():
    # Get item name to update from the user
    name = input("Enter the name of the item to update: ")

    # Search for the item in the CSV file
    found = False
    updated_items = []
    with open(DATA_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == name.lower():
                print("Item found! Enter the updated details:")
                new_name = input("Enter updated item name: ")
                new_price = float(input("Enter updated item price: "))
                new_quantity = int(input("Enter updated item quantity: "))
                updated_items.append([new_name, new_price, new_quantity])
                found = True
            else:
                updated_items.append(row)

    # Rewrite the updated data to the CSV file
    with open(DATA_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_items)

    if found:
        print("Item updated successfully!")
    else:
        print("Item not found!")

# Function to remove an item from the grocery list
def remove_item():
    # Get item name to remove from the user
    name = input("Enter the name of the item to remove: ")

    # Search for the item in the CSV file and remove it
    found = False
    updated_items = []
    with open(DATA_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() != name.lower():
                updated_items.append(row)
            else:
                found = True

    # Rewrite the updated data to the CSV file
    with open(DATA_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_items)

    if found:
        print("Item removed successfully!")
    else:
        print("Item not found!")

# Function to search for an item in the grocery list
def search_item():
    # Get item name to search from the user
    name = input("Enter the name of the item to search: ")

    # Search for the item in the CSV file
    found = False
    with open(DATA_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == name.lower():
               
