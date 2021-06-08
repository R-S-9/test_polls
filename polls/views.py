from django.shortcuts import render


def index(request):
    hello = 'hi'

    return render(request, 'main_page.html', context={'hi': hello})
