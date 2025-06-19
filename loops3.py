# Control statements when using while-loops


count = 0
while count <= 5:
    count += 1
    if count == 3:
        break # Stop after 3.
    print(count)

print()

count = 0
while count <= 5:
    count += 1
    if count == 3:
        continue # The value (3) will be skipped.
    print(count)

print()

count = 0
while count <= 5:
    count += 1
    if count == 3:
        pass # The value (3) will be skipped.
    print(count)