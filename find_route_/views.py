from django.shortcuts import render


def home(request):
    name = "Bob"
    context = {'name': name}
    return render(request, 'home.html', context)
