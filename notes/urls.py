from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addnote/$', views.addNote, name='addNote'),
    url(r'^about/$', views.about, name='about')
]
