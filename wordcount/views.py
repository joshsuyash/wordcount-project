from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def COUNT(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()
    words=dict()
    for word in wordlist:
        if word not in words:
            words[word]=1
        else:
            words[word] +=1
    print(words)
    bigcount = None
    bigword = None
    for word,count in words.items():
        if bigcount is None or count> bigcount:
            bigcount = count
            bigword = word

    return render(request,'count.html',{'fulltext':fulltext ,'COUNT':len(wordlist) , 'wordcount':words.items()  ,'Maxword':bigword , "Maxwordcount":bigcount })
def Newcount(request):
    return render(request,'home.html')
