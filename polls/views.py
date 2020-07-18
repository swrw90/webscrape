from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Question


# Each view takes a request object and question_id to lookup a specific question using its primary key.
# Load the index.html and use context dictionary key  to pass the list of questions to the frontend.
def index(request):
    latest_question_list = Question.objects.order_by('-publication_date')[:5] #Reverse order list of 5 questions by publication date to get most recent.
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html/', context) #Sends request and context to index.html

# Try to get question by its primary key and pass it via context dictionary to details.html, otherwise raise 404 error. 
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #primary key = question_id
    return render(request, '/polls/detail.html', {'question': question})

def  results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)  