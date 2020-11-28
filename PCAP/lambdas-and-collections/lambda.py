
print("FUNCTION:")
### - multiple expression

def addition(var1, var2):
    print("This is from the function: ", end="")    # expression 1
    sum = var1 + var2                               # expression 2
    return sum                                      # expression 3

print(addition(2,2))

print("\nLAMBDA: ", end="")
### - only one expression

lambda_add = lambda variable1, variable2: variable1 + variable2                   # Single expression (implcitly always returned)
# variabe = lambda(keyword) parameter1, parameter2 ...: <expression>

print(lambda_add(3, 3))