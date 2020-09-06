#!/usr/local/bin/python3.8

print('Tuples')

# another sequence in python, like lists

print ('\nTuples are Immutable!')       # i.e. it has a fixed length


# EXAMPLES
point = (1.0, 3.0)                      # x,y coordinates

# point[0] = 2.0                        # error: immutable = cannot change the tuple (cannot reassign)
#                                       unlike list, this ensures that a particular item can not be modified

point_3d = point + (4.0,)               # adds the 3rd coordination
#                                       (4.0,) instead of (4.0) to show it's a tuple, not math operation (bidmas)

x, y, z = point_3d                      # tuples allow you to break the items into their own variables (unpacked) - less common with list

print (  x  )                           # 1.0
print (  y  )                           # 3.0
print (  z  )                           # 4.0

print (x, y, z)                         # 1.0 3.0 4.0

print ('My name is: %s %s' % ('Nabeel', 'Hamad'))   # python2.0 specific but a good example of the use of tuples
#                                                   'Nabeel' and 'Hamad' are tuples that were assigned (unpacked) to %s and $s respectively

