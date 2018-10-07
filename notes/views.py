from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'notes/home.html', {
        'page_title': 'Home'
    })

def addNote(request):
    return render(request, 'notes/addNote.html', {
        'page_title': 'Add Note'
    })
    
def about(request):
    return render(request, 'notes/about.html', {
        'page_title': 'About'
    })