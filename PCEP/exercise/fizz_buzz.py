# Limit the numbers from 0 - 100

users_input = int(input("Enter an integer value: "))

if users_input in range(0, 100 + 1):
    pass
else:
    print("Please enter a number between 0 - 100")
    exit(1)

if users_input % 3 == 0 and users_input % 5 == 0:
    print("FizzBuzz")
elif users_input % 3 == 0:
    print("Fizz")
elif users_input % 5 == 0:
    print("Buzz")
else:
    print(users_input)
