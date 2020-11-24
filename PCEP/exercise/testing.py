def name_function(name1, name2):
    var1 = f"The users firstname is {name1}\n"
    var2 = f"The users secondname is {name2}"
    return var1 + var2

output = name_function(name2="Hamad", name1="Nabeel")

print(output)


def driver_function(name, car_name="Mercedez"):
    return f"{name} is able to drive the car {car_name} \
he's just worried about driving the car"

output_2 = driver_function("Nabeel")
print(output_2)

##########################
print("\nScoping\n")
##########################

y = 20

def setting_y(y):
    print("Inner y is:", y)
    global x
    x = 30

setting_y(10)
print("Outter y is:", y)
print("X is set inside a function:", x)