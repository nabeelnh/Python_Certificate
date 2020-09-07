#!/usr/local/bin/python3.8

# 1) Write a `split_name` function that takes a string and returns a dictionary with first_name and last_name

def split_name(name):
    names = name.split()
    first_name = names[0]
    last_name = names[-1]

    return {
        'first_name': first_name, 
        'last_name': last_name,
    }

assert split_name("Kevin Bacon") == {
    "first_name": "Kevin",
    "last_name": "Bacon",
}, f"Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}"

# 2) Ensure that `split_name` can handle multi-word last names
def split_name(name):
    names = name.split(maxsplit=1)
    first_name = names[0]
    last_name = names[-1]
    
    return {
        'first_name': first_name, 
        'last_name': last_name,
    }

assert split_name("Victor Von Doom") == {
    "first_name": "Victor",
    "last_name": "Von Doom",
}, f"Expected {{'first_name': 'Victor', 'last_name': 'Von Doom'}} but received {split_name('Victor Von Doom')}"

# 3) Write an `is_palindrome` function to check if a string is a palindrome (reads the same from left-to-right and right-to-left)
def is_palindrome(name):
    return name == name[::-1]

assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
assert is_palindrome("stop") == False, f"Expected False but got {is_palindrome('stop')}"

# 4) Make `is_palindrome` work with numbers
def is_palindrome(name):
    names = str(name)
    return names == names[::-1]

assert is_palindrome(101) == True, f"Expected True but got {is_palindrome(101)}"
assert is_palindrome(10) == False, f"Expected False but got {is_palindrome(10)}"

# 5) Write a `build_list` function that takes an item and a number to include in a list
# def build_list(item, number=1):
#     my_list = []
#     return my_list + [item] * number

def build_list(item, number=1):
    my_list = []

    for each_element in range(number):
        my_list.append(item)
    
    return my_list

assert build_list("Apple", 3) == [
    "Apple",
    "Apple",
    "Apple",
], f"Expected ['Apple', 'Apple', 'Apple'] but received {repr(build_list('Apple', 3))}"
assert build_list("Orange") == [
    "Orange"
], f"Expected ['Orange'] but received {repr(build_list('Orange'))}"