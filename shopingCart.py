# # Shopping Cart - Milestone Version 1.0

# # first we create an empty list to store item names
# cart = []
# print("Welcome to the Shopping Cart Program!")
# # We will display a menu to the user with options to add items, view the cart, or quit
# # and we will loop until the user chooses to quit.

# while True:
#     # Display the menu
#     print("\nWhat would you like to do?: ")
#     print("1. Add item")
#     print("2. View cart")
#     print("3. Quit")

#     # Get user choice
#     choice = input("Please enter an option: ")

#     if choice == "1":
#         # Add item
#         item = input("What item would you like to add? ")
#         cart.append(item)
#         print(f"'{item}' has been added to the cart.")
    
#     elif choice == "2":
#         # View cart
#         print("\nThe contents of the shopping cart are:")
#         for item in cart:
#             print(f"- {item}")
    
#     elif choice == "3":
#         # Quit which is the exit option.
#         print("Thank you for shopping. Goodbye!")
#         break
    
#     else:
#         print("Invalid option. Please try again.")


Improved Shopping Cart with Edge Case Handling and File Saving
Shopping Cart App by Michael Attah
This program helps users manage a shopping cart by adding, removing, and totaling items with prices. It also saves the cart to a file on exit.
Shopping Cart App by Michael Attah.

item_names = []
item_prices = []

def show_cart():
    if not item_names:
        print("Your cart is empty.")
    else:
        print("\nThe contents of the shopping cart are:")
        for i in range(len(item_names)):
            print(f"{i+1}. {item_names[i]} - ${item_prices[i]:.2f}")

def save_to_file():
    with open("shopping_cart_summary.txt", "w") as f:
        f.write("Shopping Cart Summary:\n")
        for i in range(len(item_names)):
            f.write(f"{i+1}. {item_names[i]} - ${item_prices[i]:.2f}\n")
        f.write(f"\nTotal: ${sum(item_prices):.2f}\n")

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    choice = input("Please enter an option: ")

    if choice == "1":
        name = input("What item would you like to add? ")
        try:
            price = float(input(f"What is the price of '{name}'? "))
            item_names.append(name)
            item_prices.append(price)
            print(f"'{name}' and it's price '{price}' has been added to the cart.")
        except ValueError:
            print("Invalid price! Please enter a number (e.g., 19.99).")

    elif choice == "2":
        show_cart()

    elif choice == "3":
        if not item_names:
            print("Your cart is empty.")
        else:
            show_cart()
            try:
                remove_index = int(input("Which item would you like to remove? ")) - 1
                if 0 <= remove_index < len(item_names):
                    removed_item = item_names.pop(remove_index)
                    item_prices.pop(remove_index)
                    print(f"'{removed_item}' has been removed from the cart.")
                else:
                    print("Sorry, that is not a valid item number.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    elif choice == "4":
        total = sum(item_prices)
        print(f"The total price of the items in the cart is: ${total:.2f}")

    elif choice == "5":
        save_to_file()
        print("Cart saved to your 'shopping Cart'. ")
        print("Thank you for shopping with us. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")