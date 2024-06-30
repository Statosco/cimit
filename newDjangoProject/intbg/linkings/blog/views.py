from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts =[
    {
        'author':'coreyMS',
        'title':'Blog Post 1',
        'content': 'First post content',
        'date_posted':'August 27, 2018'
    },
    {
        'author':'jane doe',
        'title':'Blog Post 2',
        'content': 'Secont post content',
        'date_posted':'August 17, 2018'
    },
]

def home(request):
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
