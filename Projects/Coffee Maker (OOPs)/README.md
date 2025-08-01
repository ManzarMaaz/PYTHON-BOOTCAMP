````markdown
# ☕️ Object-Oriented Coffee Machine Project

A modular, object-oriented Coffee Machine simulation written in Python.  
This version improves code organization and scalability using three custom classes:
- `CoffeeMaker` (manages resources)
- `MoneyMachine` (handles payment logic)
- `Menu` (provides drink info)

---

## 📦 Project Structure

```bash
coffee_machine/
│
├── coffee_machine.py         # Main script (this file)
├── coffee_maker.py           # CoffeeMaker class
├── money_machine.py          # MoneyMachine class
├── menu.py                   # Menu and MenuItem classes
````

---

## 🎯 Features

* Offers **Espresso**, **Latte**, and **Cappuccino**
* Modular class-based design
* Checks for sufficient ingredients
* Accepts virtual coin payments (quarters, dimes, nickels, pennies)
* Generates resource and finance reports
* Clean console interface

---

## 🚀 How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/ManzarMaaz/PYTHON-BOOTCAMP.git
   cd PYTHON-BOOTCAMP/Projects/OOP_CoffeeMachine
   ```

2. Run the main program:

   ```bash
   python coffee_machine.py
   ```

---

## 🧱 Class Overview

### `CoffeeMaker`

* `is_resource_sufficient(drink)`
* `make_coffee(drink)`
* `report()`

### `MoneyMachine`

* `make_payment(cost)`
* `report()`

### `Menu`

* `find_drink(name)`
* `get_items()`

---

## 🧪 Sample Output

```
Choose any Drink (Cappuccino, Espresso, Latte) : latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
```

---

## 🧠 Key Concepts Practiced

* Object-Oriented Programming
* Class interaction and encapsulation
* User input handling
* Financial calculations
* Resource tracking

---
