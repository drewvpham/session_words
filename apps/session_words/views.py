from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import string, random
# Create your views here.
def index(request):
    if "attempt_num" not in request.session or "word" not in request.session:
        request.session["attempt_num"] = 0
        request.session["word"] =''
        data={"attempt_num": request.session["attempt_num"], "word": request.session["word"]}

    return render(request, 'session_words/index.html')


def process(request):
    if request.method=='POST':
        new_word=get_random_string(length=14)
        print new_word
        request.session["word"]='Your random word is: '+new_word
        request.session["attempt_num"] +=1

    return render(request, 'session_words/index.html')

def reset(request):
    request.session.clear()
    return redirect("/")
