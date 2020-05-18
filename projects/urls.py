from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("about/", views.about, name="about"),
    path("sample/", views.sample, name="sample"),
    # Projects for 30projects30days
    path("clockview/", views.clockview, name="clockview"),
    path("validator/", views.validator, name="validator"),
    path("movie/", views.movie, name="movie"),
    path("custom_video_player/", views.custom_video_player, name="custom_video_player"),
]
