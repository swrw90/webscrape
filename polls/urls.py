from django.urls import path
from . import views

# When user goes to '' root url the index function from views file will run. The root path is named index.
urlpatterns = [
    path('', views.index, name='index')
]