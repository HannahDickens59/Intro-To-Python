
message = 'Bananas = R15.00, Apples = R20.00, Pears = R20.00, Oranges = R30.00, Grapes = R25.00'
print(message)

my_dict = {'Bananas': 15.00, 'Apples': 20.00, 'Pears': 20.00, 'Oranges': 30.00, 'Grapes': 25.00}

final = 00.00

num = input("Choose an item to put into your cart: ")
    
while num != "done":
    if num == "Bananas":
        final += my_dict['Bananas']
        print(f"{num} added. Current total: {final}") # Added feedback
        
    elif num == "Apples":
        final += my_dict['Apples']
        print(f"{num} added. Current total: {final}")
        
    elif num == "Pears":
        final += my_dict['Pears']
        print(f"{num} added. Current total: {final}")
        
    elif num == "Oranges":
        final += my_dict['Oranges']
        print(f"{num} added. Current total: {final}")
        
    elif num == "Grapes":
        final += my_dict['Grapes']
        print(f"{num} added. Current total: {final}")
        
    else:
        print("Invalid item. Please choose from Bananas, Apples, Pears, Oranges, or Grapes.")

    num = input("Choose another item to put into your cart, or type 'done' to cash out: ")

# Once the loop exits (num is "done")
print(f"   --- TOTAL CASH-OUT PRICE: ---")
print (f"  R{final}")



