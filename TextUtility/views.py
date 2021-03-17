# I have created this file here. -sk

from django.http import HttpResponse, Http404
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

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
        #return HttpResponse("error!")
        raise Http404("Error! Please Select an option")
