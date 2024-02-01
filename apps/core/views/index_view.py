from django.shortcuts import render


def index(request):
    data = {
        'STATIC_URL': 'static/',
        'RUN_MODE': 'PROD'
    }
    response = render(request, "index.prod.html", data)
    return response
