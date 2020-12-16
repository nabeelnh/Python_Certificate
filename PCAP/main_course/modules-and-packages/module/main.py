"""
1) Stand import
import module   
import module as mod  ## > make an alias of the import

print(module.uppercase("Nabeel"))
print(module.lowercase("Nabeel"))

2) Specify imports
from module import uppercase as up, lowercase as low

print(up("Nabeel"))
print(low("Nabeel"))

3) Import everything
from module import *

print(module.uppercase("Nabeel"))
print(module.lowercase("Nabeel"))

no 3. can lead to conflict (in variables) because you're important everything from a foreign script
- conflict: module vs script, module vs another module
"""

from module import lowercase uppercase         # enables extraction of specific things from a module
#                                               you can do alias: from module import uppercase as up, lowercase as low

import naming                                   # notes: naming module tries to import the module module from its script
#                                               , but doesn't because it's already imported on this script

print(uppercase(naming.name))
print(lowercase(naming.name))

