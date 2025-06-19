# Control statements when using for-loops  - break, continue and pass.

fruits = ["apple", "peach", "banana", "date"]

for fruit in fruits:
    if fruit == "banana":
        break # Exits loop if "banana" is found. When printed, it will stop after "peach", and will not display "banana" and "date." 
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "banana":
        continue # Skips "banana" and moves on to "date." 
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "banana":
        pass # Placeholder, no action is needed for banana. The value remains unchanged. 
    # This will be useful when you're changing specific data but want to exclude something.
    print(fruit)
    
    