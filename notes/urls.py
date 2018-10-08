from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    #add note gets the post request from the client
    #we get the form data
    url(r'^addnote/$', views.addNote, name='addNote'),
    url(r'^about/$', views.about, name='about'),
    url(r'^uploadNote/$', views.uploadNote, name='uploadNote'),

    #edit note is the url which expects a url parameter which is the noteId
    #this note id is passed to the view as the second parameter
    url(r'editNote/(?P<id>[0-9]+)/$', views.editNote, name='editNote'),
    url(r'deleteNote/(?P<id>[0-9]+)/$', views.deleteNote, name='deleteNote'),
    url(r'^saveEditedNote/(?P<id>[0-9]+)/$', views.saveEditedNote, name='saveeditednote'),

    #these are the urls 

]
