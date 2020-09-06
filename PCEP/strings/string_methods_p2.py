#!/usr/local/bin/python3.8

print ('\nString methods 2\n')

# Strings can be used as Tokens: a collection of things e.g. 


#################
# SPLIT
#################

phrase = 'This is a simple phrase'          # a Token

print (  phrase.split()  )                  # Splits the token into items in a list: ['This', 'is', 'a', 'simple', 'phrase']
#                                             default: split by space 

url = 'https://example.com/users/samantha'

users_name = url.split('/')                 # ['https:', '', 'example.com', 'users', 'samantha']

print (  users_name[-1]  )                  # Samantha


#################
# JOIN
#################

# Split a token
token = 'This is a simple token'
splitted_token = token.split()

print (  splitted_token  )                  # ['This', 'is', 'a', 'simple', 'token']

# Join back the splitted token

joined_token = ' '.join(splitted_token)     # Joined the line based of the space in between them

print (  joined_token  )                    # This is a simple token

print('\n')

#################
# FORMAT
#################

# Different inputs in the tuple
print (  'Hello my name is {} and I am learning {}'.format('Tyson', 'Python')  )

# Repeating input in the tuple
print (  'Hello my name is {0} and I am learning {1}. Much love {0}'.format('Tyson', 'Python')  )

