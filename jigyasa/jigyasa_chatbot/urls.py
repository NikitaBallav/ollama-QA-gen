from django.urls import path 

from . import views 

urlpatterns = [


    path("jigyasa", views.defaultJigyasa.as_view()),
]