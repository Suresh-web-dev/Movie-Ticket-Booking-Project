from django.urls import path
from ticket_booking_app.views import index,signup_view,login_view,logout_view,home,movies,tamil_movies,english_movies,malayalam_movies,hindi_movies,cinemas,one,tickets,sports_tickets,bookings,sports_bookings,success,sports_success,sports,my_booking,search

urlpatterns = [
    path("index/",index),
    path("signup_view/",signup_view),
    path("login_view/",login_view),
    path("logout_view/",logout_view),
    path("home/",home),
    path("movies/",movies),
    path("tamil_movies/",tamil_movies),
    path("english_movies/",english_movies),
    path("malayalam_movies/",malayalam_movies),
    path("hindi_movies/",hindi_movies),
    path("cinemas/",cinemas),
    path("sports/",sports),
    path("one/<int:id>/",one),
    path("tickets/<int:movie_id>/<int:cinema_id>/",tickets),
    path("sports_tickets/<int:sport_id>/",sports_tickets),
    path("bookings/<int:movie_id>/<int:cinema_id>/",bookings),
    path("sports_bookings/<int:sport_id>/",sports_bookings),
    path("success/<int:movie_id>/<int:cinema_id>/<str:seats>/",success),
    path("sports_success/<int:sport_id>/<str:seats>/",sports_success),
    path('my_booking/',my_booking),
    path('search/',search),
]
