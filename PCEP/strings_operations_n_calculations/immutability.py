#!/usr/local/bin/python3.8

# String are immutable i.e. they cannot be changed

print(id('key'))        # e.g. 139912821647280
print(id('keys'))       # e.g. 139912821775856

print (  id('key') == id('keys')  ) # False   