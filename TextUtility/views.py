# I have created this file here. -sk

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
#    param = {'name':'sk', 'place':'India'}
    return render(request, 'index.html')
    #return HttpResponse('hello')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'default')
    capfirst = request.POST.get('capfirst', 'default')
    uppercase = request.POST.get('uppercase', 'default')
    newlineremove = request.POST.get('newlineremove', 'default')
    charcount = request.POST.get('charcount', 'default')
    spaceremove = request.POST.get('spaceremove', 'default')

    # Analyze the text
    analyzed = ''
    purpose = ''

    if removepunc == 'on':
        analyzed = ''
        import string
        for i in djtext:
            if i not in string.punctuation:
                analyzed += i
        djtext = analyzed
        purpose += " | Remove punctuation"

    if capfirst == 'on':
        analyzed = djtext.capitalize()
        djtext = analyzed
        purpose += " | Capitalize First"

    if uppercase == 'on':
        analyzed = djtext.upper()
        djtext = analyzed
        purpose += " | Capitalize All"

    if newlineremove == 'on':
        djtext = djtext.replace('\r\n', ' ')
        purpose += " | Newline Remove"
        #print(purpose+djtext)

    if spaceremove == 'on':
        while djtext.find("  ") != -1 :
            djtext = djtext.replace('  ', ' ')
        purpose += " | Extra Space Remove"

    if charcount == 'on':
        analyzed = len(djtext)
        djtext = djtext + " \n No. of Charecter: "+str(analyzed)
        purpose += " | Character Count"


    if purpose != '':
        params = {'purpose': purpose, 'analyzed_text' : djtext}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("error!")


'''
def about(request):
    return HttpResponse('about page')

#remove punctuation
def removepunc(request):    
    #Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    #Analyze the text
    return HttpResponse("Remove punctuation <a href='/'>HOME</a>")

#capitalize first
def capfirst(request):
    return HttpResponse("capitalize first <a href='/'>HOME</a>")

#newline remove
def newlineremove(request):
    return HttpResponse("newline remove <a href='/'>HOME</a>")

#char count
def charcount(request):
    return HttpResponse("char count <a href='/'>HOME</a>")

#space remove
def spaceremove(request):
    return HttpResponse("space remove <a href='/'>HOME</a>")
'''