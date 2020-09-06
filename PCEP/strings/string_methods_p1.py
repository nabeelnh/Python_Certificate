#!/usr/local/bin/python3.8

print ('\nString methods 1\n')

my_string = 'TesTiNG'

print ( 'original string:', my_string )

print ( 'lower case:', my_string.lower() )                  # lower case

print ( 'upper case:', my_string.upper() )                  # upper case

print ( 'capitalise case:', my_string.capitalize() )        # captitalise  - first letter & make everything else lower case
#                                                             limitation: if name is McMiller = Mcmiller

long_string = 'This is a mulitword string'

print ( 'title case:', long_string.title() )                # title case  - capitalise first letter of each word


# Checks whether string is in ascii (restricted code point: 258 rather than million UTF-8)

my_string = 'TesTiNG'                   # 

print ( my_string.isascii() )           # True  - all letters are represented in ascii (0 - 128)

print ( my_string.islower() )           # False - has upper cases

print ( my_string.isupper() )           # False - has lower cases

print ( my_string.istitle() )           # False - does not have title format

print ( my_string.title().istitle() )   # True  - string --> titled it --> check if titled , thus True

print ( ' '.isspace() )                 # True  - checking for empty space


# Is it a number (float not included)

print ( 'Is it decimal:', '1'.isdecimal()  )              # True
print (  'Is it digital:', '1'.isdigit()  )               # True
print (  'Is it numeric:', '1'.isnumeric()  )             # True

# Is it alphabetical .alpha()

print ( 'Is it alphabetical:', 'abcd'.isalpha()  )        # True

# Is it alphanumeric .alnum()

print ( 'Is it alphanumeric:', 'abcd123'.isalnum()  )     # True


# Is it identifier .identifier() 
###     identifier - can it be used as a: variable, function or class

print ( 'Is it an indentifier:', 'names'.isidentifier()  )     # True    - names can be used to list a list of names

# Is it printable .printable()

print (  'Is this printable:', 'Is this printable:'.isprintable()  )           # True

print (  'Is this printable:\\n', 'Is this printable:\n'.isprintable()  )      # False  - escaped characters cannot be printed on the screen
