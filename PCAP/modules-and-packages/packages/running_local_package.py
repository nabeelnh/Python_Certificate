from local_packages.string import uppercase, lowercase        # 1) importing specifics thing
from local_packages import variable                           # 2) importing a specific module
import local_packages                                         # 3) importing the entire package                        


print(f"Uppercase Letter: {uppercase(variable.name)}")
print(f"Lowercase Letter: {lowercase(variable.name)}")

print(f"From packaged local_packages: {local_packages.string.lowercase(local_packages.variable.name)}")