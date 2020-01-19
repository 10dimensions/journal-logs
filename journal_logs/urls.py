
""" Defines URL patterns for journal_logs. """

from django.urls import path
from . import views

app_name = 'journal_logs'
urlpatterns = [    
    # Home page
    path('', views.index, name='index'), 

    # Topics Page   
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic.    
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]