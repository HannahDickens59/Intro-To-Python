
message = 'Bananas = R20.00, Apples = R24.99, Pears = R27.55, Oranges = R29.99, Grapes = R25.00'
print(message)

my_dict = {'Bananas': 20.00, 'Apples': 24.99, 'Pears': 27.55, 'Oranges': 29.99, 'Grapes': 25.00}

final = 00.00
cart_items = [] # Initialize an empty list to store items bought

num = input("Choose an item to put into your cart: ")
    
while num != "done":
    if num == "Bananas":
        final += my_dict['Bananas']
        cart_items.append(num) #Adding item to cart - bananas
        print(f"{num} added. Current total: {final}") # Added feedback
        
    elif num == "Apples":
        final += my_dict['Apples']
        cart_items.append(num)
        print(f"{num} added. Current total: {final}")
        
    elif num == "Pears":
        final += my_dict['Pears']
        cart_items.append(num)
        print(f"{num} added. Current total: {final}")
        
    elif num == "Oranges":
        final += my_dict['Oranges']
        cart_items.append(num)
        print(f"{num} added. Current total: {final}")
        
    elif num == "Grapes":
        final += my_dict['Grapes']
        cart_items.append(num)
        print(f"{num} added. Current total: {final}")
        
    else:
        print("Invalid item. Please choose from Bananas, Apples, Pears, Oranges, or Grapes.")

    num = input("Choose another item to put into your cart, or type 'done' to cash out: ")

# Once the loop exits (num is "done")

print("   ")
print("   --- YOUR CART ITEMS: ---")

print(cart_items)
print("   ")
print(f"   --- TOTAL CASH-OUT PRICE: ---")
print (f"  R{final}")



