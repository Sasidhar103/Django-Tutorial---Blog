from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'notes/home.html', {})

def addNote(request):
    return render(request, 'notes/addNote.html', {})
    
def about(request):
    return render(request, 'notes/about.html', {})