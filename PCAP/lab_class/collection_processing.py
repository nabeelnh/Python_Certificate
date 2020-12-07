# 1) Sort the `people` list of dictionaries alphabetically based on the
# 'name' key from each dictionary using the `sorted` function and store
# the new list as `sorted_by_name`

people = [
    {"name": "Kevin Bacon", "age": 61},
    {"name": "Fred Ward", "age": 77},
    {"name": "finn Carter", "age": 59},
    {"name": "Ariana Richards", "age": 40},
    {"name": "Victor Wong", "age": 74},
]

sorted_by_name = list(sorted(people, key=lambda each_dict: each_dict["name"].lower()))

assert sorted_by_name == [
    {"name": "Ariana Richards", "age": 40},
    {"name": "finn Carter", "age": 59},
    {"name": "Fred Ward", "age": 77},
    {"name": "Kevin Bacon", "age": 61},
    {"name": "Victor Wong", "age": 74},
], f"Expected sorted_by_name to equal '{sorted_by_name}' to equal '{[{'name': 'Ariana Richards', 'age': 40}, {'name': 'finn Carter', 'age': 59}, {'name': 'Fred Ward', 'age': 77}, {'name': 'Kevin Bacon', 'age': 61}, {'name': 'Victor Wong', 'age': 74}]}''"

# 2) Use the `map` function to iterate over `sorted_by_name` to generate a
# new list called `name_declarations` where each value is a string with
# `<NAME> is <AGE> years old.` where the `<NAME>` and `<AGE>` values are from
# the dictionaries.

# map(function, domain)
name_declarations = list(map(lambda each_dict: f"{each_dict['name']} is {each_dict['age']} years old", sorted_by_name))

assert name_declarations == [
    "Ariana Richards is 40 years old",
    "finn Carter is 59 years old",
    "Fred Ward is 77 years old",
    "Kevin Bacon is 61 years old",
    "Victor Wong is 74 years old",
], f"Expected name_declarations to equal '{name_declarations}' to equal '{['Ariana Richards is 40 years old', 'finn Carter is 59 years old', 'Fred Ward is 77 years old', 'Kevin Bacon is 61 years old', 'Victor Wong is 74 years old']}'"

# 3) Combine the `filter` and `sorted` functions to iterate over `sorted_by_name` to generate a
# new list called `under_seventy` that only contains the dictionaries where the
# 'age' key is less than 70, sorting the list by age.

# sorted(somethong, key=function/lambda)
# filter(function[True/False], domain)

under_seventy = sorted(
    filter(lambda each_dict: each_dict['age'] < 70, sorted_by_name),
    key=lambda each_dict: each_dict["age"]
)

assert under_seventy == [
    {"name": "Ariana Richards", "age": 40},
    {"name": "finn Carter", "age": 59},
    {"name": "Kevin Bacon", "age": 61},
], f"Expected under_seventy to equal '{under_seventy}' to equal '{[{'name': 'Ariana Richards', 'age': 40}, {'name': 'finn Carter', 'age': 59}, {'name': 'Kevin Bacon', 'age': 61}]}'"
