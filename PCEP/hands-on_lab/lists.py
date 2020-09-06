#!/usr/local/bin/python3.8

# empty list
users = []

assert users == [], f"Expected `users` to be [] but got: {repr(users)}"

# append
users.append('kevin')
users.append('bob')
users.append('alice')

assert users == ['kevin', 'bob', 'alice'], f"Expected `users` to be ['kevin', 'bob', 'alice'] but got: {repr(users)}"

print (users)

# remove item from the list
del users[1]
assert users == ['kevin', 'alice'], f"Expected `users` to be ['kevin', 'alice'] but got: {repr(users)}"

print (users)


# reverse the list and assign it to 'rev_users'
rev_users = list(reversed(users))

assert rev_users == ['alice', 'kevin'], f"Expected `rev_users` to be ['alice', 'kevin'] but got: {repr(users)}"

print (rev_users)

# add user to specific location

users.insert(1, 'melody')

assert users == ['kevin', 'melody', 'alice'], f"Expected `users` to be ['kevin', 'melody', 'alice'] but got: {repr(users)}"

print (users)


# add multipe users to a list (i.e adding two lists together)

users = users + ['andy', 'wanda', 'jim']    # or users += ['andy', 'wanda', 'jim'] 

assert users == ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'], f"Expected `users` to be ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'] but got: {repr(users)}"

print (users)


# extracting a sub-section of the list

center_users = users[2:4]

assert center_users == ['alice', 'andy'], f"Expected `users` to be ['alice', 'andy'] but got: {repr(center_users)}"

print (center_users)

print ('''
Congrats! All done''')