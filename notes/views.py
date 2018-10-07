from django.shortcuts import render, redirect
from .models import Notes
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import NoteForm

import json

# Create your views here.
def index(request):
    # data = {
    #     'page_title': 'Home',
    #     'notes': [{
    #         'title': 'Note 1',
    #         'content': 'Content of the first note is seen here'
    #     },
    #     {
    #         'title': 'Note 2',
    #         'content': 'Content of the second note is seen here'
    #     },
    #     {
    #         'title': 'Note 3',
    #         'content': 'Content of the third note is seen here'
    #     }]
    # }
    notes = Notes.objects.all()
    print (notes)
    data = {
        'page_title': 'Home',
        'notes': notes
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

def editNote(request, id):
    note = Notes.objects.filter(id=id)[0]
    return render(request, 'notes/editNote.html', {'note': note})

def deleteNote(request, id):
    Notes.objects.filter(id=id).delete()
    return redirect('index')

def saveEditedNote(request, id):
    if (request.method == 'POST'):
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = Notes.objects.filter(id=id)[0]
            note.title = form.cleaned_data['title']
            note.content = form.cleaned_data['content']
            note.image = form.cleaned_data['image']
            note.save()
        return redirect('index')
