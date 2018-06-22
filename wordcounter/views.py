from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    full_text = request.GET['full_text']
    word_list = full_text.split()

    words = {}

    for word in word_list:
        if word in words:
            #Increase
            words[word] +=1
        else:
            #Add to the dictionary "words"
            words[word] = 1

    sortedwords = sorted(words.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'full_text': full_text, 'count': len(word_list), 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')
