# Supermarket Billing System

## Overview
The **Supermarket Billing System** is a Python-based console application that allows users to generate a bill by selecting items from a predefined grocery list. The system automatically calculates discounts and applies a 5% GST before displaying the final amount.

## Features
- Predefined grocery list with item prices.
- User-friendly interface for selecting items and entering quantities.
- Automatic discount calculation:
  - 5% discount for purchases above ₹500
  - 10% discount for purchases above ₹1000
  - 15% discount for purchases above ₹2000
- 5% GST applied after discount calculation.
- Generates a detailed, well-formatted bill.
- Displays shop details, including name, address, and contact information.

## Prerequisites
- Python 3.x installed on your system.

## How to Run
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is saved.
3. Run the following command:
   ```sh
   python receipt.py
   ```
4. Follow the on-screen instructions to select items and generate the bill.

## Usage
1. The program displays a list of available grocery items with their prices.
2. Users can select items by entering the corresponding item number.
3. Users specify the quantity of each selected item.
4. Once all items are selected, the bill is generated with subtotal, discount, tax, and final total.
5. The bill also includes the shop name, address, and contact details.

## Example Output
```
==================================================
              Harikrishna Super Market
==================================================
                                    Date: 2025-03-05 14:30:00
--------------------------------------------------
Item                 Quantity   Price      Total     
--------------------------------------------------
Milk                 2         50         100       
Rice                 3         60         180       
--------------------------------------------------
Subtotal:                          ₹280.00
Discount (5%):                     ₹14.00
Subtotal after Discount:           ₹266.00
GST (5%):                          ₹13.30
Final Total:                       ₹279.30
==================================================
      Thank You for Shopping with Us!
==================================================
         123, Market Road, Hyderabad, India       
         Phone: +91-9110010100                    
==================================================
```

## Future Enhancements
- Add barcode scanning support.
- Implement a graphical user interface (GUI).
- Provide an option for dynamic item price updates.
- Integrate a database for inventory management.

## License
This project is free to use and modify for learning purpose
