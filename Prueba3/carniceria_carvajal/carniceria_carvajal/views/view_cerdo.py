from django.shortcuts import render

def cerdo(request):
    return render(request, 'cerdo.html', {})