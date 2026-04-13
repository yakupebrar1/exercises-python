# Project 5 — Mini Shopping Cart
# Author: Ebrar
# Date: April 13, 2026

menu = {
    1: ("Apple",  0.50),
    2: ("Banana", 0.30),
    3: ("Milk",   1.20),
    4: ("Bread",  2.00),
}

cart  = {}   # { item_name: quantity }
total = 0.0

# Display the menu
print("--- Shop Menu ---")
for number, (name, price) in menu.items():
    print(f"{number}. {name:<10} ${price:.2f}")
print("5. Done")

# Shopping loop
while True:
    try:
        choice = int(input("\nChoose an item (1-5): "))

        if choice == 5:
            break

        if choice in menu:
            name, price = menu[choice]

            # Add to cart: if item exists, increment; else, set to 1
            if name in cart:
                cart[name] += 1
            else:
                cart[name] = 1

            # Update total price
            total += price
            print(f"Added {name} to your cart.")
        else:
            print("Invalid choice, try again.")

    except ValueError:
        print("Please enter a valid number (1-5).")

# Print the receipt
print("\n--- Receipt ---")
if not cart:
    print("Your cart is empty.")
else:
    for item, qty in cart.items():
        # Find the price from the menu to show the math on the receipt
        # We search the menu values for the item name
        item_price = next(price for name, price in menu.values() if name == item)
        print(f"{item:<10} x{qty}   ${item_price * qty:.2f}")

print("-" * 20)
print(f"Total: ${total:.2f}")
print("Thank you!")
