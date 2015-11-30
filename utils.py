import re

def findname(question):
	"""
    Return a list of valid names (first, last, or both) given a string of text.
    If two names are connected by and, it will return both. Otherwise, it will
    return the first name in the string.

    Arguments:
      question: A string of text

    Returns:
      An empty list or a list of valid names

    >>> findname("")
    []

    >>> findname("Angela stuff")
    ['Angela']
    
    >>> findname("stuff Serena stuff")
    ['Serena']

    >>> findname("Angela and Serena")
    ['Angela', 'Serena']

    >>> findname("Angela and Serena stuff")
    ['Angela', 'Serena']

    >>> findname("Angela Serena")
    ['Angela Serena']

    >>> findname("Angela Serena hello")
    ['Angela Serena']

    >>> findname("Angela not Serena")
    ['Angela']

    >>> findname("Angela and Serena not Zamansky")
    ['Angela', 'Serena']

    >>> findname("Angela , Serena and Zamansky")
    ['Angela', 'Serena', 'Zamansky']
    """
	regex = [A-Z]([a-z]+|\.)(?:\s+[A-Z]([a-z]+|\.))*(?:\s+[a-z][a-z\-]+){0,2}\s+[A-Z]([a-z]+|\.)
	person = re.findall(pattern, line)


if __name__=="__main__":
    import doctest
    doctest.testmod()