from .models import sign,log,image_upload,events_upload,sports_upload,cinemas_upload,book
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages





# Create your views here.

def home(request):
    all_datas = image_upload.objects.all()
    obj = {"all" :all_datas}
    return render(request,"home.html",obj)



def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        user = User.objects.create_user(username=username,email=email,password=password2)
        login(request,user)

        sign.objects.create(username=username,email=email,password1=password1,password2=password2)
        obj={"username":username,"email":email,"password1":password1,"password2":password2}
    return render(request,"home.html",obj)


def signup_datas(request):
    all_datas=sign.objects.all()
    obj={"all":all_datas}
    return render(request,"view_datas/signup_datas.html",obj)



def login_view(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        
        log.objects.create(username=username,password=password)
        obj={"username":username,"password":password}
        if user is not None:
            login(request,user)
            return redirect(home)

        else:
            messages.error(request,"invalid username or password")
            return redirect(login_view)
    return render(request,"login.html")


def login_datas(request):
    all_datas=log.objects.all()
    obj={"all":all_datas}
    return render(request,"view_datas/login_datas.html",obj)


def logut_view(request):
    logout(request)
    return redirect(login_view)



def upload_movie(request):
    if request.method == "POST":
        language = request.POST.get("language")
        image = request.FILES.get("image")
        title = request.POST.get("title")
        movie_type = request.POST.get("movie_type")
        
        image_upload.objects.create(language=language,image=image,title=title,movie_type=movie_type)
        obj = {"language" : language, "image" : image, "title" : title, "movie_type" : movie_type}
        return redirect(home)
    return render(request,"admin/movie_upload_form.html")
    

def movies(request):
    all = image_upload.objects.all()
    obj = {"all" :all}
    return render(request,"movies.html",obj) 


def tamil_movies(request):
    if request.method == "POST":
        language = request.POST.get("language")
        image = request.FILES.get("image")
        title = request.POST.get("title")
        movie_type = request.POST.get("movie_type")
 
        if language.upper() == "tamil":
            image_upload.objects.create(language=language, image=image, title=title, movie_type=movie_type)
            return redirect(tamil_movies)  

   
    tamil_movie = image_upload.objects.filter(language__iexact="tamil")
    tamil =  {"all": tamil_movie}
    return render(request, "tamil_movies.html",tamil)


def english_movies(request):
    if request.method == "POST":
        language = request.POST.get("language")
        image = request.FILES.get("image")
        title = request.POST.get("title")
        movie_type = request.POST.get("movie_type")
 
        if language.upper() == "english":
            image_upload.objects.create(language=language, image=image, title=title, movie_type=movie_type)
            return redirect(english_movies)  

   
    english_movie = image_upload.objects.filter(language__iexact="english")
    english =  {"all": english_movie}
    return render(request, "english_movies.html",english)




def malayalam_movies(request):
    if request.method == "POST":
        language = request.POST.get("language")
        image = request.FILES.get("image")
        title = request.POST.get("title")
        movie_type = request.POST.get("movie_type")
 
        if language.upper() == "malayalam":
            image_upload.objects.create(language=language, image=image, title=title, movie_type=movie_type)
            return redirect(malayalam_movies)  

   
    malayalam_movie = image_upload.objects.filter(language__iexact="malayalam")
    malayalam =  {"all": malayalam_movie}
    return render(request, "malayalam_movies.html",malayalam)




def hindi_movies(request):
    if request.method == "POST":
        language = request.POST.get("language")
        image = request.FILES.get("image")
        title = request.POST.get("title")
        movie_type = request.POST.get("movie_type")
 
        if language.upper() == "hindi":
            image_upload.objects.create(language=language, image=image, title=title, movie_type=movie_type)
            return redirect(hindi_movies)
           

    hindi_movie = image_upload.objects.filter(language__iexact="hindi")
    hindi =  {"all": hindi_movie}  
    return render(request, "hindi_movies.html",hindi)



def upload_events(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        title = request.POST.get("title")
        location = request.POST.get("location")
        
        events_upload.objects.create(image=image,title=title,location=location)
        obj = {"image" : image, "title" : title, "location" : location}
        return redirect(events)
    return render(request,"admin/events_upload_form.html")


def events(request):
    all = events_upload.objects.all()
    obj = {"all" :all}
    return render(request,"events.html",obj)




def upload_sports(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        title = request.POST.get("title")
        location = request.POST.get("location")
        sports_type = request.POST.get("sports_type")
        
        sports_upload.objects.create(image=image,title=title,location=location,sports_type=sports_type)
        obj = {"image" : image, "title" : title, "location" : location,"sports_type" : sports_type}
        return redirect(sports)
    return render(request,"admin/sports_upload_form.html")


def sports(request):
    all = sports_upload.objects.all()
    obj = {"all" :all}
    return render(request,"sports.html",obj)





def upload_cinemas(request):
    if request.method == "POST":
        cinemas_name = request.POST.get("cinemas_name")
        address = request.POST.get("address")
        
        cinemas_upload.objects.create(cinemas_name=cinemas_name,address=address)
        obj = {"cinemas_name" : cinemas_name,"address" : address}
        return redirect(cinemas)
    return render(request,"admin/cinemas_upload_form.html")


def cinemas(request):
    all = cinemas_upload.objects.all()
    obj = {"all" :all}
    return render(request,"cinemas.html",obj)


def movie_ticket(request,id):
    all = cinemas_upload.objects.all()
    x=image_upload.objects.get(id=id)
    obj = {"all" :all,"x":x}
    return render(request,"cinemas.html",obj)
   
   


def admin_page(request):
    return render(request,"admin/admin.html")



def apply(request):
    return render(request,"apply.html")



def one(request,id):
    a=image_upload.objects.get(id=id)
    x={"a":a}
    return render(request,"movie_book.html",x)



def two(request,id):
    b=events_upload.objects.get(id=id)
    x={"b":b}
    return render(request,"event_book.html",x)



def three(request,id):
    c=sports_upload.objects.get(id=id)
    x={"c":c}
    return render(request,"sports_book.html",x)





def search(request):
    if request.method=="POST":
        title = request.POST.get("title").upper()
        if title:
            results = image_upload.objects.filter(title=title)
            if results.exists():
                obj = {"all": results}
                return render(request, "movies.html",obj)
            else:
                obj = {"error": "No movies found."}
                return render(request, "movies.html",obj)
    return render(request, "movies.html")




def event_search(request):
    if request.method=="POST":
        title = request.POST.get("title").upper()
        if title:
            results = events_upload.objects.filter(title=title)
            if results.exists():
                obj = {"all": results}
                return render(request, "events.html",obj)
            else:
                obj = {"error": "No event found."}
                return render(request, "events.html",obj)
    return render(request, "events.html")




def sports_search(request):
    if request.method=="POST":
        title = request.POST.get("title").upper()
        if title:
            results = sports_upload.objects.filter(title=title)
            if results.exists():
                obj = {"all": results}
                return render(request, "sports.html",obj)
            else:
                obj = {"error": "No sports found."}
                return render(request, "sports.html",obj)
    return render(request, "sports.html")




def cinemas_search(request):
    if request.method=="POST":
        cinemas_name = request.POST.get("cinemas_name").upper()
        if cinemas_name:
            results = cinemas_upload.objects.filter(cinemas_name=cinemas_name)
            if results.exists():
                obj = {"all": results}
                return render(request, "cinemas.html",obj)
            else:
                obj = {"error": "No cinemas found."}
                return render(request, "cinemas.html",obj)
    return render(request, "cinemas.html")




def event_success(request,id):
    x =events_upload.objects.get(id=id)
    obj = {"x":x}
    return render(request,"event_success.html",obj)



def sports_success(request,id):
    x =sports_upload.objects.get(id=id)
    obj = {"x":x}
    return render(request,"sports_success.html",obj)



def ticket_book(request):
    return render(request,"ticket_book.html")




def final_book(request,movie_id,cinema_id):
    m =image_upload.objects.get(id=movie_id)
    n = cinemas_upload.objects.get(id=cinema_id)
    obj = {"m" :m,"n":n}
    return render(request,"final_book.html",obj)



def success(request,mov_id,cin_id):
    k =image_upload.objects.get(id=mov_id)
    l = cinemas_upload.objects.get(id=cin_id)
    obj = {"k" :k,"l":l}
    
    book.objects.create(title=k.title,language=k.language,movie_type=k.movie_type,cinemas_name=l.cinemas_name)

    
    return render(request,"booking_success.html",obj)



def my_booking(request):
    all = book.objects.all()
    obj = {"all": all}
    return render(request,"my_booking.html",obj)



