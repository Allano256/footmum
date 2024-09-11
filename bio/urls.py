from django.urls import path

from . import views



urlpatterns = [
    path('bio/', views.BioList.as_view()),
    path('bio/<int:pk>', views.BioDetail.as_view()),
]
