from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.home),
    url(r'^session_words$', views.index),
    url(r'^session_words/add_word$', views.add_word),
    url(r'^session_words/reset$', views.reset)

]
