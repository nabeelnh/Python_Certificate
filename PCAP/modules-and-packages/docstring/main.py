#!/usr/bin/env python

from helpers.string import uppercase, lowercase        # 1) importing specifics thing i.e. function
from helpers import variable                           # 2) importing a specific module
import helpers                                         # 3) importing the entire package                        


print(f"Uppercase Letter: {uppercase(variable.name)}")
print(f"Lowercase Letter: {lowercase(variable.name)}")

print(f"From packaged helpers: {helpers.string.lowercase(helpers.variable.name)}")