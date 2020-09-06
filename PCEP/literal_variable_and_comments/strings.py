#!/usr/local/bin/python3.8

# single qouted string
print ('Hello')

# Double qouted string
print ("Hello")

# Multi-line string
print ("""
This
is a multi-line
string
""")

# Combining strings using + operator - this will appear on EPEL but not the script
"pass" + "word"

# To make it appear when running the script, you need to pring it
print ( "pass" + "word" )

# Mutliply operator
"ha" * 4
print ("ha" * 4)


# OBJECTS - has State + Behaviour

# state
"my string"

# beviour (method)

### Find position of letter 't' aka positional index
"my string".find('t')

### Turn string upper case
"mate sTrInG".upper()

### Turn string lower case
"mate sTrInG".lower()

# Real life example:
password = "RadicalDude"
password.lower()


# ESCAPE SEQUENCES

# new line (n)
print ( "Hello \ngood looking\nmotherfucker" )

# tab (t)
print ( "Hello \tgood looking\tmotherfucker" )

# Escaping the excape (\\)
print ( "Hello \\ngood looking\\nmotherfucker" )

# QOUTES

# single in double
print ( "Hello 'good looking' " )

# double in single
print ( 'Hello "good looking" ' )

# double in double - escaping
print ( "\"Double\" in double" )
