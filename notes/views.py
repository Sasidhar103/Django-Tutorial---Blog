from django.shortcuts import render, redirect
from .models import Notes
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import NoteForm

import json

# Create your views here.
def index(request):
    data = {
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
    }
    return render(request, 'notes/home.html', data)

def addNote(request):
    return render(request, 'notes/addNote.html', {
        'page_title': 'Add Note'
    })
    
def about(request):
    return render(request, 'notes/about.html', {
        'page_title': 'About'
    })

@csrf_exempt
def uploadNote(request):
    if (request.method == 'POST'):
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            note = Notes(title = title, content = content, image = image)
            note.save()
        return redirect('index')
