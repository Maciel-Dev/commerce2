from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import User, Items



def index(request):
    return render(request, "auctions/index.html", {
        "items": Items.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def createListing(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("desc")
        category = request.POST.get("category")
        initialBid = request.POST.get("bidInitial")
        imageLink = request.POST.get("image")
   
        item = Items(title=f"{title}", description=f"{description}",
        category=f"{category}", initialBid= f"{initialBid}" ,imageLink=f"{imageLink}")
        item.save()

    return render(request, "auctions/createListing.html")

def pageLoad(request, nameItem):
    allItem = Items.objects.all()
    for item in allItem:
        if nameItem in item.title:
            return render(request, "auctions/pageItems.html",{
            "item": item.title
            })

            
    
