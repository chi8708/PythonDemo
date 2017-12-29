
# from django.http import HttpResponse


# def hello(request):
#     return HttpResponse("Hello django!")

from django.shortcuts import render


def hello(request):
    context = {}
    context["hello"] = "hello django1!"
    return render(request, 'hello.html', context)
