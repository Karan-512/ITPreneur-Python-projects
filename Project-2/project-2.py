import qrcode


# ---------- CLASS DEFINITIONS (CRUD) ----------

class Order:
    def __init__(self, order_name, quantity, price):
        self.order_name = order_name
        self.quantity = quantity
        self.price = price
    def __str__(self):
        total = self.quantity * self.price
        return f"{self.id}. {self.order_name} x{self.quantity} — Rs. {total}"

class OrderManager():
    def __init__(self):
        self.orders = {}
        self.next_id = 1

    def create_task(self, order_name, quantity, price):
        order = Order(order_name, quantity, price)
        order.id = self.next_id
        self.orders[self.next_id] = order
        self.next_id += 1

        return f"✅ Added: {order.order_name} x{order.quantity} (Rs. {order.price} each)"

    def read_all_orders(self):
        if not self.orders:
            print("No items in your order yet!!!")
        else:
            print("\n" + "=" * 60)
            print("Your Orders:")
            print("\n" + "=" * 60)
            for order in self.orders.values():
                print("   ", order)

    def order_by_id(self, id):
        order = self.orders.get(id)
        if order:
            print("\nOrder found:")
            print("   ", order)
        else:
            print(f"\nOrder #{id} not found.")

    def update_order(self,id):
        order = self.orders.get(id)
        if not order:
            print(f"\nOrder #{id} not found.")
            return
        print("\nWhat do you want to update?")
        print("1. Change Item")
        print("2. Change Quantity")
        print("3. Change Both")

        choice = int(input("Enter choice (1-3): "))

        # --- CHANGE ITEM ---
        if choice == 1 or choice == 3:
            print("\nSelect New Category:")
            print("1. Coffees\n2. Starters\n3. Main Course\n4. Desserts")
            cat = int(input("Enter (1-4): "))

            if   cat == 1: menu = coffees
            elif cat == 2: menu = starters
            elif cat == 3: menu = main_dishes
            elif cat == 4: menu = dessert
            else:
                print("Invalid category!")
                return

            print("\nSelect New Dish:")
            items = list(menu.keys())

            sr = 1
            for item in menu.keys():
                print(f"{sr}. {item} — Rs. {menu[item]}")
                sr += 1

            dish_choice = int(input("Enter option: "))
            new_name = items[dish_choice - 1]
            new_price = menu[new_name]

            order.order_name = new_name
            order.price = new_price

        # Changing quantity
        if choice == 2 or choice == 3:
            new_quantity = int(input("Enter new quantity: "))
            order.quantity = new_quantity

        print("\n Order Updated Successfully!")
        print("   ", order)

    def remove_order(self, id):
        if id in self.orders:
            removed = self.orders.pop(id)
            print(f"\nRemoved: {removed.order_name} x{removed.quantity}")
        else:
            print(f"\nOrder #{id} not found.")




# ---------- MENU DATA ----------

starters = {
    "Crispy Potato Wedges             ": 149,
    "Cheesy Garlic Bread              ": 179,
    "Peri-Peri Chicken Bites          ": 229,
    "Paneer Tikka Skewers             ": 199,
    "Loaded Nachos with Salsa & Cheese": 189,
    "Classic Veg Spring Rolls         ": 159
}

main_dishes = {
    "Grilled Chicken Steak with Herb Sauce ": 349,
    "Paneer Butter Masala with Butter Naan ": 299,
    "Spaghetti Aglio e Olio                ": 279,
    "Veggie Burger with Fries              ": 249,
    "Classic Margherita Pizza (10”)        ": 299,
    "Thai Green Curry with Steamed Rice    ": 329
}

dessert = {
    "Chocolate Brownie with Ice Cream        ": 179,
    "Classic Cheesecake                      ": 199,
    "Tiramisu Cup                            ": 219,
    "Red Velvet Pastry                       ": 169,
    "Choco Lava Cake                         ": 159,
    "Waffles with Maple Syrup & Whipped Cream": 189
}

coffees = {
    "Espresso             ": 99,
    "Cappuccino           ": 149,
    "Café Latte           ": 159,
    "Mocha                ": 179,
    "Cold Coffee (Classic)": 169,
    "Caramel Frappe       ": 199
}


# ---------- ORDER MANAGER OBJECT ----------
order_manager = OrderManager()


# ---------- FUNCTIONS ----------

def generateBill():
    if not order_manager.orders:
        print("\n You did not order anything!!")
        return
    total = 0

    print("\n" + "=" * 60)
    print("\t\t☕ THE WIRED MUG CAFÉ ☕\t\t ")
    print("=" * 60)
    print("\n📝 Your Bill Summary:\n")

    for order in order_manager.orders.values():
        item_total = order.price * order.quantity
        print(f"\t• {order.order_name} x{order.quantity} — Rs. {item_total}")
        total += item_total

    print("-" * 60)
    print(f"\tTotal Amount — Rs. {total}")
    print("=" * 60)

    payment(total)


def payment(total):
    print("\n💳  Payment Options")
    print("-" * 40)
    print("1️⃣ Credit/Debit Card\n2️⃣  UPI\n3️⃣  Cash\n")
    pay_mode = int(input("Select your payment method (1-3): "))

    match pay_mode:
        case 1:
            print("\n💳 Card Payment Selected")
            input("Enter Card Number: ")
            input("Enter CVV: ")
            input("Enter Expiry (MM/YY): ")
            print("\n✅ Payment Successful via Card!")
        case 2:
            print("\n📱 Please scan the QR code below to pay via UPI:\n")
            upi_link = f"upi://pay?pa=karandaniel@ybl&pn=The%20Wired%20Mug%20Cafe&am={total}&cu=INR"

            qr = qrcode.QRCode(
                version=1,
                box_size=2,
                border=2
            )
            qr.add_data(upi_link)
            qr.make(fit=True)
            qr.print_ascii(invert=True)
            print("\n(Scan with any UPI app to pay)")
            print("\n✅ Payment Successful via UPI!")
        case 3:
            print("\n💵 Please pay the amount at the counter.")
            print("\n✅ Payment Successful via Cash!")

    print("\n" + "=" * 60)
    print("🎉  THANK YOU FOR VISITING THE WIRED MUG CAFÉ!  🎉")
    print("✨  Have a wonderful day!  ✨")
    print("=" * 60 + "\n")


def menuItems(menu):
    while True:
        print("\n" + "-" * 60)
        print("🍽️  MENU")
        print("-" * 60)
        sr = 1
        for item in menu.keys():
            print(f"{sr}. {item} — Rs. {menu[item]}")
            sr += 1
        print("7. Exit\n")
        print("-" * 60)

        choice = int(input("Select item (1-7): "))
        if choice == 7:
            return

        quantity = int(input("Enter quantity: "))
        item_name = list(menu.keys())[choice - 1]
        price = menu[item_name]

        print(order_manager.create_task(item_name, quantity, price))


# ---------- MAIN LOOP ----------

while True:
    print("\n" + "=" * 60)
    print("☕  WELCOME TO THE WIRED MUG CAFÉ  ☕")
    print("=" * 60)
    print("\n🍴  Select a Category:\n")
    print("1️⃣  Coffees\n2️⃣  Starters\n3️⃣  Main Course\n4️⃣  Desserts")
    print("5️⃣  View Orders\n6️⃣  Remove Order\n7️⃣  View Order by #\n8️⃣  Update Order by #")
    print("9️⃣  Generate Bill & Exit\n")
    choice = input("Enter your choice (1-8): ")

    match choice:
        case "1":
            print("\n---------- COFFEES ----------")
            menuItems(coffees)
        case "2":
            print("\n---------- STARTERS ----------")
            menuItems(starters)
        case "3":
            print("\n---------- MAIN COURSES ----------")
            menuItems(main_dishes)
        case "4":
            print("\n---------- DESSERTS ----------")
            menuItems(dessert)
        case "5": order_manager.read_all_orders()
        case "6":
            order_manager.read_all_orders()
            id = int(input("Enter Order number to delete: "))
            order_manager.remove_order(id)
        case "7":
            id = int(input("Enter Order number: "))
            order_manager.order_by_id(id)
        case "8":
            order_manager.read_all_orders()
            id = int(input("\nEnter the Order number you want to update: "))
            order_manager.update_order(id)
        case "9":
            generateBill()
            break
        case _:
            print("❌ Invalid Choice!")