from django.shortcuts import render
from bot.models import Message
from bot.robot import NiceRobot, MeanRobot
import random

# Create your views here.
def index_view(request):
    return render(request, 'index.html', {})

#Nice view, handles logic for Nice robot. 
def nice_view(request):
    if request.method == 'POST':
        robo = NiceRobot('Nice Bender')
        text, author_name = request.POST['text'], "you"
        #Responds differently based on given text
        if text != '' :
            response = None
            Message.objects.create(text=text, author=author_name)
            if text.lower() == "what time is it" or text.lower() == "what time is it?":
                response = robo.give_time()
            elif text.lower() == "rock" or text.lower() == "paper" or text.lower() == "scissors":
                response = robo.rockPaperScissors()
            elif text.lower() == "add" or text.lower() == "subtract" or text.lower() == "multiply" or text.lower() == "divide":
                response = robo.doMath()
            else:
                response = robo.respond(text)
            Message.objects.create(text=response, author=robo.name)
    messages = Message.objects.all()
    messages = list(reversed(messages))
    return render(request, 'nice.html', {'messages': messages })

#Nice view, handles logic for mean robot. 
def mean_view(request):
    if request.method == 'POST':
        robo = MeanRobot('Mean Bender')
        text, author_name = request.POST['text'], "you"
        #Responds differently based on given text
        if text != '' :
            response = None
            Message.objects.create(text=text, author=author_name)
            if text.lower() == "what time is it" or text.lower() == "what time is it?":
                response = robo.give_time()
            elif text.lower() == "rock" or text.lower() == "paper" or text.lower() == "scissors":
                response = robo.rockPaperScissors()
            elif text.lower() == "add" or text.lower() == "subtract" or text.lower() == "multiply" or text.lower() == "divide":
                response = robo.doMath()
            else:
                response = robo.respond(text)
            Message.objects.create(text=response, author=robo.name)
    messages = Message.objects.all()
    messages = list(reversed(messages))
    return render(request, 'mean.html', {'messages': messages })

