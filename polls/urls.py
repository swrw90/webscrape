from django.urls import path
from . import views

# Each path function returns a response matching the url input. <int:question_id> is used to dynamically match any pattern input.
urlpatterns = [
    # /polls
    path('', views.index, name='index'),
    # /polls/5
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/5/results 
    path('<int:question_id>/results/', views.results, name='results'),
    # /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote')
]