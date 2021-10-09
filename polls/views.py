from django import template
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, response,HttpResponseRedirect,Http404
from django.template import context, loader
from django.urls import reverse
from django.views import generic 

from .models import Question,Choice

# Create your views here.

'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        #return last five published questions
        return Question.objects.order_by('-pub_date')[:5]

'''def detail(request,question_id):
    #ry:
        #question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
        #raise Http404("Question does not exist!!")
    #return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk= question_id)
    return render(request, 'polls/detail.html',{'question':question})'''

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

'''def results(request,question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})'''

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request,question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        #Redisplay the question voting form
        return render(request,'polls/detail.html',{'question':question,'error_message': "You didn't select a choice!",})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        #Always return a Http response after successfully dealing with POST data to prevent data from being posted twice if a user hits the back button
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


