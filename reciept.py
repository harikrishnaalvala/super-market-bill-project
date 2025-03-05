from datetime import datetime

# Shop details
SHOP_NAME = "Harikrishna Super Market"
SHOP_ADDRESS = "123, Market Road, Hyderabad, India"
CONTACT_NUMBER = "Phone: +91-9110010100"

# Predefined grocery list with prices
grocery_list = {
    1: ("Milk", 50),
    2: ("Bread", 30),
    3: ("Rice", 60),
    4: ("Sugar", 40),
    5: ("Salt", 20),
    6: ("Eggs", 6),  # Per egg price
    7: ("Butter", 120),
    8: ("Cheese", 150),
    9: ("Chicken", 250),
    10: ("Fruits", 80)  # Mixed fruit price per kg
}

# Function to display available grocery items
def display_grocery_list():
    print("\nAvailable Grocery Items:")
    print("=" * 40)
    for key, (item, price) in grocery_list.items():
        print(f"{key}. {item} - ₹{price} per unit/kg")
    print("=" * 40)

# Function to calculate discount
def calculate_discount(total):
    if total > 2000:
        return 0.15  # 15% discount
    elif total > 1000:
        return 0.10  # 10% discount
    elif total > 500:
        return 0.05  # 5% discount
    return 0  # No discount

# Function to display the bill
def generate_bill(items):
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print("\n" + "=" * 50)
    print(f"{SHOP_NAME.center(50)}")  # Shop name centered
    print("=" * 50)
    print(f"{'Date:'.rjust(40)} {date_time}")  # Date & Time aligned right
    print("-" * 50)
    print("{:<20} {:<10} {:<10} {:<10}".format("Item", "Quantity", "Price", "Total"))
    print("-" * 50)

    total_amount = 0
    for item, details in items.items():
        quantity, price = details
        total = quantity * price
        total_amount += total
        print("{:<20} {:<10} {:<10} {:<10}".format(item, quantity, price, total))

    # Calculate discount
    discount_rate = calculate_discount(total_amount)
    discount_amount = round(total_amount * discount_rate, 2)
    subtotal_after_discount = total_amount - discount_amount

    # Apply tax (e.g., 5% GST)
    tax = round(subtotal_after_discount * 0.05, 2)
    final_amount = subtotal_after_discount + tax

    print("-" * 50)
    print(f"{'Subtotal:':<30} ₹{total_amount:.2f}")
    print(f"{'Discount (' + str(int(discount_rate * 100)) + '%):':<30} ₹{discount_amount:.2f}")
    print(f"{'Subtotal after Discount:':<30} ₹{subtotal_after_discount:.2f}")
    print(f"{'GST (5%):':<30} ₹{tax:.2f}")
    print(f"{'Final Total:':<30} ₹{final_amount:.2f}")
    print("=" * 50)
    print("      Thank You for Shopping with Us!")
    print("=" * 50)
    print(f"{SHOP_ADDRESS.center(50)}")  # Address centered at bottom
    print(f"{CONTACT_NUMBER.center(50)}")  # Contact number centered
    print("=" * 50)

# Main function to take user input
def main():
    items = {}
    print("Welcome to Supermarket Billing System!")
    
    while True:
        display_grocery_list()
        try:
            choice = int(input("\nSelect an item by number (or 0 to finish): "))
            if choice == 0:
                break
            if choice not in grocery_list:
                print("Invalid selection! Please choose a valid item number.")
                continue

            item_name, item_price = grocery_list[choice]
            quantity = int(input(f"Enter quantity of {item_name}: "))
            if quantity < 1:
                print("Quantity must be at least 1!")
                continue

            if item_name in items:
                items[item_name] = (items[item_name][0] + quantity, item_price)
            else:
                items[item_name] = (quantity, item_price)

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if items:
        generate_bill(items)
    else:
        print("No items purchased. Thank you!")

# Run the program
if __name__ == "__main__":
    main()
