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
    path("video/", views.video, name="video"),
    path("exchange_rate/", views.exchange_rate, name="exchange_rate"),
    path("dom_array/", views.dom_array, name="dom_array"),
    path("landing_page/", views.landing_page, name="landing_page"),
    path("hangman/", views.landing_page, name="hangman"),
]
