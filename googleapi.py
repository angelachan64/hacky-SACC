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

    >>> findname("Angela and Serena stuff")
    ['Angela', 'Serena']

    >>> findname("Angela Serena")
    ['Angela Serena']

    >>> findname("Angela Serena hello")
    ['Angela Serena']
    """

    wordlist = []
    hold = []
    temp = ""
    held = False
    for word in question.split():
        if not held:
            if not word.islower():
                hold.append(word)
                held = True
        else:
            if not word.islower():
                hold.append(" ")
                hold.append(word)
                temp = ''.join(hold)
                wordlist.append(temp)
                hold = []
                held = False
                temp = ""
            else:
                temp = ''.join(hold)
                wordlist.append(temp)
                hold = []
                held = False
                temp = ""
    if held:
        temp = ''.join(hold)
        wordlist.append(temp)
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
    #return  withcap

def questiontype(question):
    """
    Return the question word given a string of text

    Arguments:
      question: A string of text

    Returns:
      An empty list or a list of valid question words

    >>> questiontype("")
    ''

    >>> questiontype("Who is Angela")
    'Who'
    
    >>> questiontype("Hubbada hubba whee")
    ''

    >>> questiontype("Who what Where When Why?")
    'Who'

    >>> questiontype("who is Serena??")
    'who'
    """
    types = ['who', 'what', 'where', 'when', 'why', 'how']
    wlist = question.split()
    if wlist:
        if wlist[0].lower() in types:
            return wlist[0]
        else:
            return ""
    else:
        return ""

    # for word in question.split():
    #     if word in types:
    #         questionlist.append(word)
    # return questionlist


if __name__=="__main__":
    import doctest
    doctest.testmod()
