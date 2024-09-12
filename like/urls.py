from django.urls import path
from .  import views


urlpatterns = [
    path('like/',views.LikeList.as_view()),
    path('like/<int:pk>/', views.LikeDetail.as_view()),
]

