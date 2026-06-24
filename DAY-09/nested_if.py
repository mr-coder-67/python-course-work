# Available products with their stock counts (0 means out of stock)
products = {
    'laptop': 0,
    'mouse': 10,
    'charger': 5,
    'phone': 30,
    'keyboard': 0,
}

# Ask the user for the product name (exact key expected)
product = input("enter the product: ")

# First check: is the product present in our catalog?
if product in products:
    # Nested check: is the product in stock (non-zero quantity)?
    if products[product] != 0:
        # Product exists and is available
        print(f"You can buy {product}!!")
    else:
        # Product exists but stock is zero
        print(f"{product} is out of stock")
else:
    # Product key not found in catalog
    print(f"{product} is not available")
