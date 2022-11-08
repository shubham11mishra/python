from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
articles = {
    'sports': 'sports page',
    'finance': 'finnace page',
    'politics': 'politics pagge'

}


def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:

        raise Http404('404 GENERIC ERROR')


def num_page_view(request, id):
    topic_list = list(articles.keys())
    topic = topic_list[id]
   
    return HttpResponseRedirect(reverse('topic-page',args =[topic]))


def first_app(request):
    return HttpResponse('first app')


def sports_view(request):
    return HttpResponse('sports page')


def finance_view(request):
    return HttpResponse("finance page")


def add_view(request, num1, num2):
    return HttpResponse(num1+num2)
