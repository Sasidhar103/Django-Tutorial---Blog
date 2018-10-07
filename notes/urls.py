from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addnote/$', views.addNote, name='addNote'),
    url(r'^about/$', views.about, name='about'),
    url(r'^uploadNote/$', views.uploadNote, name='uploadNote'),
    url(r'editNote/(?P<id>[0-9]+)/$', views.editNote, name='editNote'),
    url(r'deleteNote/(?P<id>[0-9]+)/$', views.deleteNote, name='deleteNote'),
    url(r'^saveEditedNote/(?P<id>[0-9]+)/$', views.saveEditedNote, name='saveeditednote'),

]
