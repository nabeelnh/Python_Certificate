#!/usr/local/bin/python3.8

# INDEXING 

##  extracting the character from a string by providing it's position within the string.
##  'string'[<position_of_the_string>]

print ( 'name'[0] )                 # 'n'

name = 'nabeel'
print ( name[2] )                   # 'b'

# Using len
print ( name[ len(name) -1 ] )      # from the end (length of name) - 1 i.e. 'l'

#print ( name[len(name)] )          # this will not work because len(name) = 6 i.e. out of this strings index range

# Going opposite direction
print ( name[-1] )                  # 'l'  because it starts from the opposite direction 'nabeel'


# SLICING

##  allows us to specify ranges of indexing to work with
##  'string'[<starting_indext>:<index_just_outside_of_the_letter_we_want>]

name = 'SeifHamoud'

print ( name[0:4] )            # Seif 

print ( name[4:10] )           # Hamoud 

print ( name[4:len(name)] )    # Hamoud 

print ( name[4:] )             # Hamoud 

# STEP VALUE
##  Specify initial position, final position, jumping steps
##  'string'[<intial_position>:<final_position + 1>:<jumping_steps>]

long_name = 'Hello_This_is_a_long_name'

print ( long_name[6:len(long_name)] )            # This_is_a_long_name
print ( long_name[6:] )                          # alternative of This_is_a_long_name

print ( long_name[6:len(long_name):2] )          # Ti_saln_ae
print ( long_name[6::2] )                        # alternative of Ti_saln_ae

print ( long_name[::2] )                         # HloTi_saln_ae

# Reversing the order of a string

print ( 'Nabeel'[::1] )                          # Nabeel  (default)

print ( 'Nabeel'[::-1] )                         # leebaN
