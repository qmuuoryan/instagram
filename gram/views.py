from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf.urls import url,include
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm,ProfileForm,CommentForm
from django.conf.urls.static import static
from .models import Profile,Image,Comments
from django.contrib.auth.models import User
from .import models
from annoying.decorators import ajax_request
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from friendship.models import Friend,Follow,Block


@login_required(login_url='/accounts/login')
def welcome(request):
    all_images = Image.objects.all()
    all_users = Profile.objects.all()
    comments = Comments.objects.all()
    next = request.GET.get('next')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        image_id = int(request.POST.get("Ryan"))
        post = Project.objects.get(id = image_id)
        if form.is_valid():
            comment = Form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('welcome')
        else:
            form = CommentForm()
    if next: return redirect(next)
    return render(request, 'all-gram/welcome.html',  locals())

@login_required(login_url='/accounts/login/')
def follow(request,user_id):
    users = User.objects.get(id = user_id)
    follow = Follow.objects.add_follower(request.user,users)
    return redirect('welcome',  locals())

@login_required(login_url='/accounts/login/')
def unfollow(request,user_id):
    users = User.objects.get(id = user_id)
    follow = Follow.objects.remove_follower(request.user,users)
    return redirect('welcome',  locals())

@login_required(login_url='/accounts/login/')
def explore(request):
    return render(request, 'all-gram/explore.html',  locals())

@login_required(login_url='/accounts/login/')
def notification(request):
    return render(request, 'all-gram/notification.html',  locals())

@login_required(login_url='/accounts/login/')
def profile(request):
    images = Image.objects.all()
    pr = Profile.objects.all()
      
    current_user = request.user
    posts = Image.objects.all()
    image_form = ProfileForm()
    if request.method == 'POST':
        image_form =ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if image_form.is_valid:
            image_form.save()
        else:
            image_form = ProfileForm()
            return render(request, 'all-gram/userprofile.html',{"pr":pr},  locals())
    return render(request, 'all-gram/userprofile.html',{"pr":pr},  locals())

@login_required(login_url='/accounts/login')
def upload(request):
    current_user = request.user
    p = Profile.objects.filter(id=current_user.id).first()
    imageuploader_profile = Image.objects.filter(imageuploader_profile=p).all()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.imageuploader_profile= p
            post.save()
            return redirect('/')
    else:
        form =PostForm
    return render(request, 'all-gram/upload.html', {"form": form},  locals())

def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'all-gram/search.html',{"message":message,"profiles": searched_profiles})
    else:
        message = "You haven't searched for anyone"
        return render(request, 'all-gram/search.html',{"message":message})