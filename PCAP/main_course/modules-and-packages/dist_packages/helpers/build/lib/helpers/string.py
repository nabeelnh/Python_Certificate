# filter(condition, domain)

def uppercase(name):
    return list(filter(str.isupper, name))

def lowercase(name):
    return list(filter(str.islower, name))


if __name__ == "__main__":                  # This ensure the print statement is only printed when calling this script directly
    print("Hello from the module.py")       # not as a module to be imported