x = 1

try:
    print(x)
    
except NameError:
    print("Variable x is not defined")

#except: #if there is an error in the code
    #print("Something went wrong.")
    
#finally: #shows weather or not there is an error in the code.
    #print("The 'try except' is finished.")

else:
    print("Something went wrong.")
    
    
x = 1

if x <0:
    raise Exception ("Sorry, no numbers below 0 are accepted.")
