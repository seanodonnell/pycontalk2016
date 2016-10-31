from django.http import HttpResponse

def index(request):
    a = 5
    b = 2
    raise Exception("Hello Pycon")
    return HttpResponse("Hello Pycon")
