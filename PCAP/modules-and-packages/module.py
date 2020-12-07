# filter(condition, domain)


__all__ = ['uppercase']                     
# WAYS TO HIDE MODULE ENTITY - (works only with: from module import *)
# 1) __all__ = ['uppercase'] 

# specify module entity that can be called with "__all__" list
# 2) being variable, function, class with "_"
# e.g "_uppercase" instead of "uppercase"

# if user specifies the specific entity when calling the module without using *
# rather than "from module import *" they use "from module import _uppercase" then nothing will prevent the module from being extracted.


def uppercase(name):
    return list(filter(str.isupper, name))

def lowercase(name):
    return list(filter(str.islower, name))


if __name__ == "__main__":                  # This ensure the print statement is only printed when calling this script directly
    print("Hello from the module.py")       # not as a module to be imported