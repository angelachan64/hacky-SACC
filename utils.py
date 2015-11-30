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
    []
    
    >>> findname("stuff Serena Chan stuff")
    [('Serena', 'Chan')]

    >>> findname("Angela Chan and Serena Chan")
    [('Angela', 'Chan'), ('Serena', 'Chan')]

    >>> findname("Angela Chan Serena Chan")
    [('Angela', 'Chan'), ('Serena', 'Chan')]

    >>> findname("Angela Chan Serena Chan Mike Zamansky")
    [('Angela', 'Chan'), ('Serena', 'Chan'), ('Mike', 'Zamansky')]
    """
        pattern = "([A-Z][a-z]*)[\s-]([A-Z][a-z]*)"
        person = re.findall(pattern, question)
        return person


if __name__=="__main__":
    import doctest
    doctest.testmod()
