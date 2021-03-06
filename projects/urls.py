from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("project_index/", views.project_index, name="project_index"),
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
    path("speech_reader/", views.speech_reader, name="speech_reader"),
    path("speak_number/", views.speak_number, name="speak_number"),
    path("car_driving_game/", views.car_driving_game, name="car_driving_game"),
    path("expense_tracker/", views.expense_tracker, name="expense_tracker"),
    path("music_player/", views.music_player, name="music_player"),
    path("typing_game/", views.typing_game, name="typing_game"),
    path("meal_finder/", views.meal_finder, name="meal_finder"),
    path("hi_lo/", views.hi_lo, name="hi_lo"),
    path("floppy_bird/", views.floppy_bird, name="floppy_bird"),
    path("xy_plotter/", views.xy_plotter, name="xy_plotter"),
    #backtesting paths
    path("btindex/", views.btindex, name="btindex"),
    path("bt_ex1/", views.bt_ex1, name="bt_ex1"),
    path("bt_ex2/", views.bt_ex2, name="bt_ex2"),
    path("bttest/", views.bttest, name="bttest"),
]
