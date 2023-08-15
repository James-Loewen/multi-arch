import os

from django.http import HttpResponse


def hello_world(request):
    return HttpResponse(
        '<h1 style="color: tomato;">Hello from Django!</h1><p>This time with red!</p>'
    )


def secret_code(request):
    secret_code = os.getenv("SECRET_CODE", None)
    if secret_code:
        return HttpResponse(f"<code>Secret Code: {secret_code}</code>")
    else:
        return HttpResponse("<code>No secrets!</code>")
