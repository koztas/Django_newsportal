from django.urls import path
from .views import *

urlpatterns = [
    path('authorList/', AuthorList.as_view()),
    path('post/<int:pk>/', Post.as_view()),
]
