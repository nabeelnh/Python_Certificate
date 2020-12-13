# A function can take multiple expressions
def addition(var1, var2):
    return var1 + var2

print (addition(5, 5))

# A lambda can take only a single expression
addition = lambda var1, var2: var1 + var2
print (addition(10, 10))