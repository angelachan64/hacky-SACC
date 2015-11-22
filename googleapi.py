import google, urllib2, bs4, re


def search(question):
    if not question:
        return
    results = google.search(question, num=10, start=0, stop=10)
    
    rlist = []
    
    for r in results:
        rlist.append(r)
    
    return rlist
