def uppercase(name):
    """
    This function will list out all the uppercase letters
    from a given string

    # DocTest below
    >>> uppercase("Nabeel Hamad")
    ['N', '']
    """
    return list(filter(str.isupper, name))

def lowercase(name):
    return list(filter(str.islower, name))


