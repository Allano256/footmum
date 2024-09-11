from django.urls import path
from . import views



urlpatterns = [
    path('broadcast/',views.BroadcastList.as_view()),
    path('broadcast/<int:pk>',views.BroadcastList.as_view()),

]
