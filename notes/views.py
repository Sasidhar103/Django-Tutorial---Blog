from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'notes/home.html', {
        'page_title': 'Home',
        'notes': [{
            'title': 'Note 1',
            'content': 'Content of the first note is seen here'
        },
        {
            'title': 'Note 2',
            'content': 'Content of the second note is seen here'
        },
        {
            'title': 'Note 3',
            'content': 'Content of the third note is seen here'
        }]
    })

def addNote(request):
    return render(request, 'notes/addNote.html', {
        'page_title': 'Add Note'
    })
    
def about(request):
    return render(request, 'notes/about.html', {
        'page_title': 'About'
    })