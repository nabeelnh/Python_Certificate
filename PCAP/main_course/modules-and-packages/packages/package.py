from packages.string import uppercase, lowercase        # 1) importing specifics thing
from packages import variable                           # 2) importing a specific module
import packages                                         # 3) importing the entire package                        


print(f"Uppercase Letter: {uppercase(variable.name)}")
print(f"Lowercase Letter: {lowercase(variable.name)}")

print(f"From packaged packages: {packages.string.lowercase(packages.variable.name)}")