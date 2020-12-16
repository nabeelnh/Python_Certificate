# Using String
def output(name):
    return f"The name is {name}"
print(output("Nabeel"))

output = lambda name: f"the name is {name}"
print(output("Ahmed"))

# Using intergers
def output(num):
    return f"{num} square is: {num * num}"
print(output(10))

output = lambda num: f"{num} square is: {num * num}"
print(output(5))


"""
Function vs Lambda

- Lambda's don't have a name
- Lambda's take only ONE expression
"""