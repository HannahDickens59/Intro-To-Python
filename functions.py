#They encapsulate a piece of code and allow you to reuse it throughout your program.
'''
def greet(name):
    print(f"Hello, {name}")

greet("Joshua")

def add(a, b):
    return a + b

result = add(5, 8)
print(result)
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")
    
greet("Jordan", "Good Morning")
