class CartItem:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def additem(self):
        self.quantity += 1
        print(f"{self.item_name} added to cart. Quantity: {self.quantity}")

    def removeitem(self):
        print(f"{self.item_name} removed from cart.")

    def calculate_total(self):
        total = self.price * self.quantity
        return total

cart_items = []

while True:
    print("\nShopping Cart Menu:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Calculate Total")
    print("4. Exit")
    
    menu = input("Select an option: ")
    
    if menu == "1":
        try:
            item_name = input("Enter item name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            item = CartItem(item_name, price, quantity)
            cart_items.append(item)
            print(f"{item.item_name} added to cart.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the price and quantity.")
    
    elif menu == "2":
        try:
            if cart_items:
                for i, item in enumerate(cart_items):
                    print(f"{i+1}. {item.item_name} - Quantity: {item.quantity}")
                item_index = int(input("Enter item number to remove: ")) - 1
                if 0 <= item_index < len(cart_items):
                    cart_items[item_index].removeitem()
                    cart_items.pop(item_index)
                else:
                    print("Invalid item number.")
            else:
                print("No items in cart.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    elif menu == "3":
        if cart_items:
            print("Items in cart:")
            for item in cart_items:
                print(f"{item.item_name} - Quantity: {item.quantity} - Total: ${item.calculate_total()}")
            total = sum(item.calculate_total() for item in cart_items)
            print(f"Total Price for all items: ${total}")
        else:
            print("No items in cart.")
    
    elif menu == "4":
        break
    
    else:
        print("Invalid option. Please select a valid option.")