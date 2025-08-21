from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from .models import movies_upload,cinemas_upload,sports_upload,book
# Create your views here.

def index(request):
    return render(request,"signup_pages/index.html")

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username=username,email=email,password=password)
        login(request,user)
        return redirect(home)
    return render(request,"signup_pages/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect(home)

        else:
            messages.error(request,"invalid username or password")
            return redirect(login_view)
    return render(request, "signup_pages/login.html")

def logout_view(request):
    logout(request)
    return redirect(login_view)

def home(request):
    all = movies_upload.objects.all()
    obj = {"all" :all}
    return render(request,"main/home.html",obj)

def movies(request):
    all = movies_upload.objects.all()
    obj = {"all" :all}
    return render(request,"main/movies.html",obj)


def tamil_movies(request):
    tamil_movie = movies_upload.objects.filter(language ="tamil")
    tamil = {"all" : tamil_movie}
    return render(request,"main/tamil_movies.html",tamil)

def english_movies(request):
    english_movie = movies_upload.objects.filter(language ="english")
    english = {"all" : english_movie}
    return render(request,"main/english_movies.html",english)

def malayalam_movies(request):
    malayalam_movie = movies_upload.objects.filter(language ="malayalam")
    malayalam = {"all" : malayalam_movie}
    return render(request,"main/malayalam_movies.html",malayalam)

def hindi_movies(request):
    hindi_movies = movies_upload.objects.filter(language ="hindi")
    hindi = {"all" : hindi_movies}
    return render(request,"main/hindi_movies.html",hindi)


def cinemas(request):
    return render(request,"main/cinemas.html")



def sports(request):
    all = sports_upload.objects.all()
    obj = {"all" :all}
    return render(request,"main/sports.html",obj)


def one(request,id):
    a = movies_upload.objects.get(id=id)
    all = cinemas_upload.objects.all()
    obj = {"all" : all,"a":a}
    return render(request,"main/cinemas.html",obj)



def tickets(request,movie_id,cinema_id):
    movie = movies_upload.objects.get(id=movie_id)
    cinems = cinemas_upload.objects.get(id=cinema_id)
    obj = {"movie" : movie,"cinema":cinems}
    return render(request,"main/tickets.html",obj)


def sports_tickets(request,sport_id):
    sport = sports_upload.objects.get(id=sport_id)
    obj = {"sport":sport}
    return render(request,"main/sports_tickets.html",obj)


def bookings(request,movie_id,cinema_id):
    movie = movies_upload.objects.get(id=movie_id)
    cinema = cinemas_upload.objects.get(id=cinema_id)
    if request.method == "POST":
        seats = request.POST.get("seats")
        obj = {"movie": movie,"cinema": cinema,"seats": seats,}
        return render(request,"main/bookings.html",obj)
    return render(request, "main/bookings.html", {"movie": movie, "cinema": cinema})


def sports_bookings(request,sport_id):
    sport = sports_upload.objects.get(id=sport_id)
    if request.method == "POST":
        seats = request.POST.get("seats")
        obj = {"sport": sport,"seats": seats,}
        return render(request,"main/sports_bookings.html",obj)
    return render(request,"main/sports_bookings.html", {"sport": sport})



def success(request,movie_id,cinema_id,seats):
    movie =movies_upload.objects.get(id=movie_id)
    cinema = cinemas_upload.objects.get(id=cinema_id)

    book.objects.create(user=request.user,image=movie.image,title=movie.title,language=movie.language,movie_type=movie.movie_type,cinemas_name=cinema.cinemas_name,seats=seats)
    obj = {"movie": movie, "cinema": cinema, "seats": seats}
    return render(request,"main/success.html",obj)


def sports_success(request,sport_id,seats):
    sport = sports_upload.objects.get(id=sport_id)
    book.objects.create(user=request.user,image=sport.image,title=sport.title,location=sport.location,sports_type=sport.sports_type,seats=seats)
    obj = {"sport": sport, "seats": seats}
    return render(request,"main/sports_success.html",obj)


def my_booking(request):
    all = book.objects.filter(user=request.user)
    obj = {"all": all}
    return render(request,"main/my_bookings.html",obj)


def search(request):
    if request.method == "POST":
        title = request.POST.get("title").upper()
        if title:
            result = movies_upload.objects.filter(title=title) or sports_upload.objects.filter(title=title)
            if result.exists():
                obj = {"all" : result}
                return render(request,"main/movies.html",obj)
            else:
                obj = {"error" : "Movies Not Found"}
                return render(request,"main/movies.html",obj)
    return render(request,"main/movies.html")
            