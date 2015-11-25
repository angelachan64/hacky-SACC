import re


def search(question):
    if not question:
        return
    results = google.search(question, num=10, start=0, stop=10)
    
    rlist = []
    
    for r in results:
        rlist.append(r)
    
    return rlist

def findname(question):
    """
    Return a list of valid names (first, last, or both) given a string of text

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

    >>> findname("Angela Serena")
    ['Angela Serena']

    >>> findname("Angela Serena hello")
    ['Angela Serena']
    """

    wordlist = []
    hold = ""
    held = False
    for word in question.split():
        if not held:
            if not word.islower():
                hold = word
                held = True
        else:
            if not word.islower():
                hold.append(' ')
                hold.append(word)
                wordlist.append(hold)
                hold = ""
                held = False
            else:
                wordlist.append(word)
    return wordlist
                
    #withcap = []
    #without = []
    #for word in question.split():
    #    if word.islower():
    #        without.append(word)
    #    else:
    #        withcap.append(word)
    #onelist = withcap + without
    #for word in onelist:
    #    print (word)
    return  withcap

if __name__=="__main__":
    import doctest
    doctest.testmod()
