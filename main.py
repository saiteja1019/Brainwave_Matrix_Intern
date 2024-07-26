class InventoryManagementSystem:
    def __init__(self):
        self.users = {"admin": "password"}  # Default admin credentials
        self.inventory = {}

    def authenticate(self):
        print("User Authentication")
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username in self.users and self.users[username] == password:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed. Try again.")
            return False

    def add_product(self):
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        quantity = self.get_positive_integer("Enter product quantity: ")
        price = self.get_positive_float("Enter product price: ")

        self.inventory[product_id] = {'name': name, 'quantity': quantity, 'price': price}
        print(f"Product {name} added successfully.")

    def edit_product(self):
        product_id = input("Enter product ID to edit: ")
        
        if product_id in self.inventory:
            name = input("Enter new product name: ")
            quantity = self.get_positive_integer("Enter new product quantity: ")
            price = self.get_positive_float("Enter new product price: ")

            self.inventory[product_id] = {'name': name, 'quantity': quantity, 'price': price}
            print(f"Product {name} updated successfully.")
        else:
            print("Product ID not found.")

    def delete_product(self):
        product_id = input("Enter product ID to delete: ")

        if product_id in self.inventory:
            del self.inventory[product_id]
            print(f"Product {product_id} deleted successfully.")
        else:
            print("Product ID not found.")

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for product_id, details in self.inventory.items():
                print(f"ID: {product_id}, Name: {details['name']}, Quantity: {details['quantity']}, Price: {details['price']}")


    def low_stock_alerts(self):
        threshold = self.get_positive_integer("Enter low stock threshold: ")
        print("Low Stock Alerts:")
        for product_id, details in self.inventory.items():
            if details['quantity'] < threshold:
                print(f"ID: {product_id}, Name: {details['name']}, Quantity: {details['quantity']}")

    def get_positive_integer(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    raise ValueError("Value must be a positive integer.")
                return value
            except ValueError as e:
                print(e)

    def get_positive_float(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                if value < 0:
                    raise ValueError("Value must be a positive float.")
                return value
            except ValueError as e:
                print(e)

    def main_menu(self):
        while True:
            print("\nInventory Management System")
            print("1. Add Product")
            print("2. Edit Product")
            print("3. Delete Product")
            print("4. View Inventory")
            print("5. Low Stock Details")
            print("6. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.add_product()
            elif choice == 2:
                self.edit_product()
            elif choice == 3:
                self.delete_product()
            elif choice == 4:
                self.view_inventory()
            elif choice == 5:
                self.low_stock_alerts()
            elif choice == 6:
                print("Exiting Inventory Management System.")
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    ims = InventoryManagementSystem()
    if ims.authenticate():
        ims.main_menu()

if __name__ == "__main__":
    main()
