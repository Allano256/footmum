from django.urls import path
from . import views

urlpatterns = [
    path('follower/', views.FollowerList.as_view()),
    path('follower/<int:pk>', views.FollowerDetail.as_view()),
]
