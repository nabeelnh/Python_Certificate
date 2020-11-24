users_input = input("Enter a message: ")

# Lowercase
lower_case = users_input.lower()
print("Lowercase:", lower_case)

# Uppercase
upper_case = users_input.upper()
print("Uppercase:", upper_case)

# Capitalized
capitalized_case = users_input.capitalize()
print("Capitalized:", capitalized_case)

# Title case
title_case = users_input.title()
print("Titled:", title_case)

# Splitting of words
word_split = users_input.split()
print("Words", word_split)

# Alphabetic first word
alpha_case = sorted(word_split)
first_alpha = alpha_case[0]
print("Alphabetic First Word:", first_alpha)

# Alphabetic last word
last_alpha = alpha_case[-1]
print("Alphabetic Last Word:", last_alpha)
