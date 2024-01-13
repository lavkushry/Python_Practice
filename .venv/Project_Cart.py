products = [{'name': 'Smartphone', 'price': 500, 'Description': ' A Handled Device'},
            {'name': 'table', 'price': 1000, 'Description': 'A Portable Device'},
            {'name': 'Headphone', 'price': 100, 'Description': 'A sound Device'},
            {'name': 'Smartwatch', 'price': 2000, 'Description': 'A wearable Device and Fitness Tracker'},
            {'name': 'bluetooth', 'price': 100, 'Description': 'A Wireless Sound device'}]



cart = []

while True:
    choice = input("Do you want to continue Shopping (Y/N)")
    if choice == "Y":
        print('Here is a list of products and their prices :')
        for index,product in enumerate(products):
            print(f"{index} {product['name']}:${product['price']}:{product['Description']}")

        product_id = int(input("Enter the id of You want to add"))
        # check if Product is Already present in the cart
        if products[product_id] in cart:
            products[product_id]['quantity'] += 1
        else:
            products[product_id]['quantity'] = 1
            cart.append(products[product_id])
        total=0
        print("Current Product contains are")
        for product in cart:
            print(f"{product['name']}:{product['price']}: QTY:{product['quantity']}")
            total=total+product['price']*product['quantity']
        print(f"Cart total is: {total}")

    else:
        break
print(f"Thank You, Your Final Cart are {cart}")

for product in cart:
    print(f"{product['name']}:{product['price']}")