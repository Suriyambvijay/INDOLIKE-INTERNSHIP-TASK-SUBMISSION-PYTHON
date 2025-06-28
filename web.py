users = {
    "admin": {"password": "admin123", "role": "admin"},
    "suriya": {"password": "user123", "role": "user"}
}
products = {}
cart = {}
current_user = None
def login():
    global current_user
    print("\n🔐 Login to your account")
    username = input("Username: ")
    password = input("Password: ")

    user = users.get(username)
    if user and user["password"] == password:
        current_user = {"username": username, "role": user["role"]}
        print(f"\n✅ Welcome, {username}! You are logged in as '{user['role']}'")
        return True
    else:
        print("❌ Invalid credentials. Try again.")
        return False
def add_product():
    try:
        product_id = len(products) + 1
        name = input("📦 Enter product name: ")
        price = float(input("💵 Enter price (₹): "))
        products[product_id] = {"name": name, "price": price}
        print(f"✅ Product '{name}' added successfully!")
    except ValueError:
        print("❌ Price must be a number!")
def display_products():
    if not products:
        print("\n📭 No products available right now.")
        return

    print("\n📦 Available Products:")
    for pid, item in products.items():
        print(f"{pid}. {item['name']} - ₹{item['price']}")
def add_to_cart():
    try:
        product_id = int(input("\n🛒 Enter Product ID to add to cart: "))
        if product_id not in products:
            print("❌ Product not found!")
            return

        quantity = int(input("🔢 Enter quantity: "))
        if product_id in cart:
            cart[product_id]["quantity"] += quantity
        else:
            cart[product_id] = {
                "name": products[product_id]["name"],
                "price": products[product_id]["price"],
                "quantity": quantity
            }
        print(f"✅ Added {quantity} x '{products[product_id]['name']}' to cart.")
    except ValueError:
        print("❌ Please enter valid numbers!")
def view_cart():
    if not cart:
        print("\n🛒 Your cart is currently empty.")
        return

    print("\n🛒 Items in your cart:")
    total = 0
    for item in cart.values():
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{subtotal}")
    print(f"\n💰 Total Amount: ₹{total}")
def checkout():
    if not cart:
        print("\n🛒 Cart is empty. Nothing to checkout!")
        return

    view_cart()
    print("\n✅ Order placed successfully! 🎉")
    cart.clear()
def admin_menu():
    while True:
        print("\n--- 👑 Admin Menu ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            print("👋 Logged out successfully.")
            break
        else:
            print("❌ Invalid choice. Try again.")
def user_menu():
    while True:
        print("\n--- 🙋‍♂️ User Menu ---")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            display_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            checkout()
        elif choice == "5":
            print("👋 Logged out successfully.")
            break
        else:
            print("❌ Invalid choice. Try again.")
def main():
    print("🛒 Welcome to Python E-Commerce App 🛍️")
    while True:
        if login():
            if current_user["role"] == "admin":
                admin_menu()
            else:
                user_menu()
if __name__ == "__main__":
    main()
