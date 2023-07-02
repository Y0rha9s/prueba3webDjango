from django.shortcuts import render

def vacuno(request):
    return render(request, 'vacuno.html', {})