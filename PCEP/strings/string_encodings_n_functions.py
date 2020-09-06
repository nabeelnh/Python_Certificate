#!/usr/local/bin/python3.8

print ('\nString Encoding and Functions')

# Unicode code points (the numbers behind characters)

# Strings value in code points

print ( ord('a') )              # 97


# Python 3 => Unicode by default (specifically UTF-8 encoded)
# UTF-8 stands for "Unicode Transformation Format," with the "8" meaning that values are 8-bits in length

# code points           ==>     decimal
# unicode code pints    ==>     hexadecimal


# U+2122 (unicode code points) ==>  8482 (code points)

print ( 0x2122 )                   # 8482           unicode code points --> code points

print ( ord( '\u2122' ) )          # 8482           unicode code points --> code point     
#                                  'u' stands for unicode code point

print ( '\u2122' )                 # 'TM'           unicode code points --> string

print ( chr(0x2122) )              # hexadecimal --> string     chr() function

print ( chr(8482) )                # decimal --> string     chr() function



# SUMMARY

# string --> code points 
ord('™')                            # 8482

# code points --> string
chr(8482)                           # '™'
    

# unicode code points --> code points
ord('\u2122')                       # 8482 

# unicode code points --> string
'\u2122'