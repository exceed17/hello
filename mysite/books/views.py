from django.http import HttpResponse

def index(request):
    return HttpResponse("All books in our shop")