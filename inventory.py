# =========The Shoe class=========
# Shoe class with attributes:
# Country = Country shoes are stored
# Code = Product code/ID
# Product = Product name
# Cost = Value of each Shoe object
# Quantity = Quantity of shoes stored
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Outputs cost of 'Shoe' inventory
    def get_cost(self):
        print(self.cost)

    # Outputs quantity of 'Shoe' inventory
    def get_quantity(self):
        print(self.quantity)

    # Outputs string representation of 'Shoe' object
    def __str__(self):
        print(f"Name:\t\t{self.product}"
              f"\nCode:\t\t{self.code}"
              f"\nCountry:\t{self.country}"
              f"\nValue:\t\t{self.cost}"
              f"\nQuantity:\t{self.quantity}\n")


# ==========Shoe list==========
# Stores all objects in the 'Shoe' class
shoe_list = []


# ==========Functions==========
# Reads file to create Shoe object. Shoe object is stored into 'shoe_list'
def read_shoes_data():

    try:
        # Appends each line of 'inventory.txt' as a Shoe object into 'shoe_list'
        with open("inventory.txt", "r") as inventory_file:
            inventory_file = inventory_file.readlines()[1:]
            for line in inventory_file:
                inventory = line.split(",")
                new_shoe = Shoe(inventory[0], inventory[1], inventory[2], inventory[3], inventory[4].replace("\n", ""))
                shoe_list.append(new_shoe)

    # Exception for file not found.
    # User inputs file name. File is then opened creates appends each line as a Shoe object into 'shoe_list'
    except FileNotFoundError:
        file_name = input("\nFile not found. Enter the name of the inventory file to open: ")
        with open(file_name, "r") as inventory_file:
            inventory_file = inventory_file.readlines()[1:]
            for line in inventory_file:
                inventory = line.split(",")
                new_shoe = Shoe(inventory[0], inventory[1], inventory[2], inventory[3], inventory[4])
                shoe_list.append(new_shoe)

# User inputs data of the Shoe object. Shoe object is appended to 'shoe_list'
def capture_shoes():
    country = input("Where is the product stored: ")
    code = input("Enter the product code: ")
    product = input("Enter the product name: ")
    cost = input("Enter the product cost: ")
    quantity = input("Enter the product quantity: \n")
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

# Outputs details from the __str__ function of all the objects in 'shoe_list'
def view_all():
    count = 0
    for line in shoe_list:
        count += 1
        print(count)
        Shoe.__str__(line)

# Prints the shoe with the lowest quantity. User has the choice to update the quantity.
def re_stock():
    quantity_list = []
    count = 0
    for line in shoe_list:
        quantity_list.append(int(line.quantity))
    min_quantity_index = quantity_list.index(min(quantity_list))
    try:
        for line in shoe_list:
            if count == min_quantity_index:
                Shoe.__str__(line)
            count += 1
        update_quantity = input("Would you like to update the quantity for this product? Y/N: \n")
        if update_quantity.lower() == "y":
            new_quantity = int(input("Enter the new quantity of this product in stock: \n"))
            shoe_list[min_quantity_index].quantity = new_quantity

            # Updated quantity is updated on the inventory text file.
            with open("inventory.txt", "w") as inventory_file:
                inventory_file.write("Country,Code,Product,Cost,Quantity\n")
            with open("inventory.txt", "a") as inventory_file:
                for line in shoe_list:
                    inventory_file.write(f"{line.country},{line.code},{line.product},{line.cost},{line.quantity}\n")

        # Returns to the menu if user types n, and returns re_stock if user entry is invalid.
        elif update_quantity.lower() == "n":
            return menu
        else:
            print("\nInvalid selection.")
            return re_stock()

    except ValueError:
        print("\nInvalid value. Please make sure your input is a number.\n")
        return re_stock()

# User inputs product code. Product that matches code is then printed.
def seach_shoe():
    user_shoe_entry = input("Enter the code of the product: ")
    for line in shoe_list:
        if line.code == user_shoe_entry.upper():
            Shoe.__str__(line)
            print("")
            return menu

# Outputs each Shoe object string and the total value of the objects inventory.
def value_per_item():
    for line in shoe_list:
        Shoe.__str__(line)
        value = round(float(line.cost) * float(line.quantity), 2)
        print(f"Total value for {line.product}: £{value}\n")

# Outputs the product with the highest quantity available in stock.
# Function advises this product should be put on sale.
def highest_qty():
    quantity_list = []
    count = 0
    for line in shoe_list:
        quantity_list.append(int(line.quantity))
    max_quantity_index = quantity_list.index(max(quantity_list))
    for line in shoe_list:
        if count == max_quantity_index:
            print(f"\n{line.product} is overstocked and should be put on sale.\n")
            Shoe.__str__(line)
        count += 1


#==========Main Menu=============

read_shoes_data()
# User menu. User inputs menu choice to be actioned.
while True:
    menu = input("Welcome to the menu."
                 "\n1 - Add new shoe object"
                 "\n2 - View all products"
                 "\n3 - View/Update stock of product with lowest quantity"
                 "\n4 - Search for a product"
                 "\n5 - View total value of the stock of each product"
                 "\n6 - Highest stocked product"
                 "\n7 - Exit"
                 "\nEnter an option: ")
    if menu == "1":
        capture_shoes()
    elif menu == "2":
        view_all()
    elif menu == "3":
        re_stock()
    elif menu == "4":
        seach_shoe()
    elif menu == "5":
        value_per_item()
    elif menu == "6":
        highest_qty()
    elif menu == "7":
        exit()
    else:
        print("\nInvalid selection. Please try again.")

