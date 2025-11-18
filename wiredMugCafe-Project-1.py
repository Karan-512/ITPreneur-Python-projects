import qrcode

orders = dict()

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

exit = "No"


# Functions
def getTotal(prices):
    total = 0
    for value in prices:
        total += value
    return total


def generateBill(orders):
    total = getTotal(list(orders.values()))
    print("\n" + "=" * 60)
    print("\t\t☕ THE WIRED MUG CAFÉ ☕\t\t ")
    print("=" * 60)
    print("\n📝 Your Bill Summary:\n")
    for item, price in orders.items():
        print(f"\t• {item} — Rs. {price}")
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
    orderItem = 0
    while orderItem != 7:
        print("\n" + "-" * 60)
        print("🍽️  MENU")
        print("-" * 60)
        sr = 1
        for item in menu.keys():
            print(f"{sr}. {item} — Rs. {menu[item]}")
            sr += 1
        print("7. Exit\n")
        print("-" * 60)
        orderItem = int(input("Select your order item (1-7): "))
        if orderItem == 7:
            return
        else:
            quantity = int(input("Enter Quantity: "))
            selected_item = list(menu.keys())[orderItem - 1].strip()
            print(f"\n✅ You selected: {selected_item}")
            print(f"   Quantity: {quantity}")
            print(f"   Price: Rs. {menu[list(menu.keys())[orderItem - 1]]} each")

            orders[f"{selected_item} x{quantity}"] = menu[list(menu.keys())[orderItem - 1]] * quantity
            print("🧾 Item added to your order!")



while exit.lower() != 'yes':
    print("\n" + "=" * 60)
    print("☕  WELCOME TO THE WIRED MUG CAFÉ  ☕")
    print("=" * 60)
    print("\n🍴  Select a Category:\n")
    print("1️⃣  Coffees\n2️⃣  Starters\n3️⃣  Main Course\n4️⃣  Desserts\n5️⃣  Exit\n")
    choice = input("Enter your choice (1-5): ")

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
        case "5":
            exit = 'yes'
            if not orders:
                print("\nYou did not order anything 😔")
                print("Thank you for visiting ☕ THE WIRED MUG CAFÉ ☕\nHave a lovely day! 🌸")
                break
            else:
                generateBill(orders)
                break
        case _:
            print("❌ Invalid Choice! Please try again.")
