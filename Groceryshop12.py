import json
users = []
GroceryListItems = []
cart_list = []

class groceryApp:
    # booking_count = 0

    def __init__(self, id: int, Name: str, Email: str, Password: str, Role: str):
        self.userID = id
        self.name = Name
        self.email = Email
        self.password = Password
        self.role = Role

    def hardCodedData(self):
        users.append(self)
        return users

    def validateLogin(self, email, password):
        for user in users:
            if user.email == email and user.password == password:
                return user
            else:
                return False
        return None

class GroceryList:
    def __init__(self, id, groceryname, quantity, price):
        self.groceryId = id
        self.groceryName = groceryname
        self.Quantity = quantity
        self.Price = price


class cart:
    def __init__(self, BookingID, userId, item_id, quantity, BookedAt):
        self.booking_id = BookingID
        self.userId = userId
        self.groceryDetails = item_id
        self.quantity_need = quantity
        self.booked_at = BookedAt

class groceryShowCase(groceryApp):
    def __init__(self, userid, Name, Email, Password, Role):
        super().__init__(userid, Name, Email, Password, Role)


    def grocery_for_customer(self):
        stayInCustomerMenu = True

        while(stayInCustomerMenu):
            choice = int(input("Enter your Choice: "))
            print("Customer Menu")
            print("1. Display the grocery")
            print("2. Add to cart")
            print("3. Booked History")
            print("4. Delete your history")
            print("5. Logout")
            if choice == 1:
                grocery1 = GroceryList(1, 'Sprite', '10', '20')
                grocery2 = GroceryList(2, 'Five star', '20', '40')
                grocery3 = GroceryList(3, 'Milk', '30', '60')
                GroceryListItems.append(grocery1)
                GroceryListItems.append(grocery2)
                GroceryListItems.append(grocery3)

                for grocery in GroceryListItems:
                    print(grocery.groceryId)
                    print(grocery.groceryName)
                    print(grocery.Quantity)
                    print(grocery.Price)

                    print('--------------------------')

            if choice == 2:
                booking_count = 0
                item_id = int(input("Enter the ID of your grocery: "))
                quantity = int(input("Enter the quantity: "))
                booking_data = cart(booking_count, self.userID, item_id, quantity, '12-2-2023')
                cart_list.append(booking_data)
                booking_count += 1
                print('............', cart_list)



if __name__ == "__main__":
    app = groceryApp(1, "Dharshu", "dharshu12@gmail.com", "dharshu06", "Customer")
    app.hardCodedData()
    app = groceryApp(2, "Sai", "sai6@gmail.com", "saisai2", "Admin")
    app.hardCodedData()
    app = groceryApp(3, "Pooja", "sai6@gmail.com", "saisai2", "Servicer")
    app.hardCodedData()

    login_user = app.validateLogin("dharshu12@gmail.com", "dharshu06")
    if login_user:
        if login_user.role == 'Customer':
          grocery_work = groceryShowCase(login_user.userID, login_user.name, login_user.email, login_user.password, login_user.role)
          grocery_work.grocery_for_customer()






