from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import string, random
from datetime import datetime
# Create your views here.
def home(request):
    return redirect("/session_words")

def index(request):
    return render(request, 'session_words/index.html')


def add_word(request):
    if request.method=='POST':
        word = request.POST['word']
        color = request.POST['color']

        if 'bigFont' in request.POST:
            big= request.POST['bigFont']
        else:
            big='no'


    new_word = {'word' : word,
				'color' : color,
				'big' : big,
				'created_at' :"- added on " + datetime.now().strftime("%m-%d-%Y-%H:%M %p")
				}
    if "words" not in request.session:
        request.session["words"] = []
        request.session['words'].append(new_word)
    else:
		saved_list = request.session["words"]
		saved_list.append(new_word)
		request.session['words'] = saved_list

    print request.session['words']

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect("/")
