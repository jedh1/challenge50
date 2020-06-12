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
    path("calculator/", views.calculator, name="calculator"),
    path("scrambled_words/", views.scrambled_words, name="scrambled_words"),
    path("cookies_demo/", views.cookies_demo, name="cookies_demo"),
    path("create_csv/", views.create_csv, name="create_csv"),
    path("drag_drop/", views.drag_drop, name="drag_drop"),
    path("post_scrolling/", views.post_scrolling, name="post_scrolling"),
    path("flash_cards/", views.flash_cards, name="flash_cards"),
    path("lyrics_search/", views.lyrics_search, name="lyrics_search"),
    path("breakout/", views.breakout, name="breakout"),
    path("relaxer/", views.relaxer, name="relaxer"),
    path("new_year_countdown/", views.new_year_countdown, name="new_year_countdown"),
]
