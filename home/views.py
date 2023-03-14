from django.shortcuts import render, HttpResponse 

# Create your views here.
def index(request):
    context={
        "variable" : "This is boss"
    }
    return render(request, 'index.html', context)
def about(request):
    return HttpResponse('This is my about page, bacha')
def contact(request):
    return HttpResponse('Contact me @ maanayush1002@gmail.com')
