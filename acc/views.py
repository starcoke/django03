from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib import messages


def update(request):
    if request.method == "POST":
        u = request.user
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        if up:
            u.set_password(up)
        u.comment = uc
        if pi:
            u.pic.delete()
            u.pic = pi
        u.save()
        login(request,u)
        return redirect("acc:profile")

    return render(request, "acc/update.html")


def delete(request):
    u = request.user
    ck = request.POST.get("pwck")
    if check_password(ck, u.password):
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    else:
        messages.info(request, "패스워드가 일치하지 않아 삭제되지 않습니다.")
        return redirect("acc:profile")
    
    

def profile(request):
    return render(request, "acc/profile.html")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        try:
            User.objects.create_user(username=un, password=up,
            comment=uc, pic=pi)
            return redirect("acc:login")
        except:
            messages.info(request, "유저네임 중복")
    return render(request, "acc/signup.html")

def logout_user(request):
    logout(request)
    return redirect("acc:login")

def login_user(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            messages.success(request, f"WELCOME {u}🎈")
            return redirect("acc:index")
        else:
            messages.error(request, "계정정보가 일치하지 않습니다.")

    return render(request, "acc/login.html")

def index(request):
    return render(request, "acc/index.html")