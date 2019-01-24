from django.shortcuts import render
import operator
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dic = {}
    
    for word in words:
        if word[-1] == '.' or word[-1] == ',' or word[-1] == '?' or word[-1] == '!' or word[-1] == '"' or word[-1] == "'" or word[-1] == ')':
            word = word[:len(word)-1]
        elif word[0] == '(' or word[0] == '"' or word[0] == "'":
            word = word[1:]
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    return render(request, 'result.html', {'fulltext' : text,'total':len(words), 'words':word_dic.items()})