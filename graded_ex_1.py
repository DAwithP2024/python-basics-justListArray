# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_categories():
    for index, category in enumerate(products, start=1):
        print(f"{index}. {category}")
    try:
        choice = int(input("Select a category: ")) - 1
        if 0 <= choice < len(products):
            return choice
    except ValueError:
        pass
    return None


def display_products(products_list):
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price}")


def display_sorted_products(products_list, sort_order):
    if sort_order == "desc":
        sorted_list = sorted(products_list, key=lambda x: x[1], reverse=True)
    if sort_order == "asc":
        sorted_list = sorted(products_list, key=lambda x: x[1], reverse=False)
    display_products(sorted_list)
    return sorted_list


def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))


def display_cart(cart):
    total = 0
    for product, price, quantity in cart:
        cost = price * quantity
        total += cost
        print(f"{product} - ${price} x {quantity} = ${cost}")
    print(f"Total cost: ${total}")
    return total


def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")


def validate_name(name):
    return len(name.split(" ")) == 2 and all(part.isalpha() for part in name.split())


def validate_email(email):
    return "@" in email


def main():
    name = input("Enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid first and last name.")
        name = input("Enter your name: ")

    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email: ")

    cart = []
    while True:
        category_index = display_categories()
        if category_index is None:
            print("Invalid selection. Please try again.")
            continue

        category_name = list(products.keys())[category_index]
        product_list = products[category_name]

        display_products(product_list)

        print("\nOptions:")
        print("1. Select a product to buy")
        print("2. Sort the products according to the price")
        print("3. Go back to the category selection")
        print("4. Finish shopping")
        choice = input("Choose an option: ")

        if choice == "1":
            product_choice = input("Enter the number of the product you want to buy: ")
            product_index = int(product_choice) - 1
            if 0 <= product_index < len(product_list):
                quantity = input("Enter the quantity: ")
                if quantity.isdigit() and int(quantity) > 0:
                    add_to_cart(cart, product_list[product_index], int(quantity))
                else:
                    print("Invalid quantity.")
            else:
                print("Invalid product number.")

        elif choice == "2":
            order = input("Sort by price: 1 for ascending, 2 for descending: ")
            if order == "1":
                display_sorted_products(product_list, "asc")
            elif order == "2":
                display_sorted_products(product_list, "desc")
            else:
                print("Invalid option.")

        elif choice == "3":
            break

        elif choice == "4":
            if cart:
                total_cost = display_cart(cart)
                address = input("Enter delivery address: ")
                generate_receipt(name, email, cart, total_cost, address)
            else:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
            return
        else:
            print("Invalid choice.")


""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
