from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("<h1>Hello from Django!</h1><p>This time with paragraph text!</p>")