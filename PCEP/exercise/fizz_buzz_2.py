
users_input = int(input("How many values should we process: "))

if users_input in range(1, 100+1):
    pass
else:
    print(f"The number {users_input} is outside of the range")
    exit(1)

for each_number in range(1, users_input + 1):
    if each_number % 3 == 0 and each_number % 5 == 0:
        print("FizzBuzz")
    elif each_number % 3 == 0:
        print("Fizz")
    elif each_number % 5 == 0:
        print("Buzz")
    else:
        print(each_number)
