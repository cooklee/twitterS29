from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from twitter_app.models import User, Tweet

def index(request):
    return render(request, 'base.html')


def add_user(request):
    if request.method == 'GET':
        return render(request, 'add_user.html')
    username = request.POST['username']
    password = request.POST['password']
    re_password = request.POST['password2']
    if password == re_password:
        User.objects.create(username=username, password=password)
        return HttpResponse('udało sie')
    else:
        return render(request, 'add_user.html', {'username': username, 'message': 'hasła nie sa te same'})


def show_users(request):
    users = User.objects.all().order_by('username')
    return render(request, 'user_list.html', {'users': users})

def add_tweet(request):
    if request.method == 'GET':
        users = User.objects.all()
        return render(request, 'add_tweet.html', {'users':users})
    text = request.POST['text']
    user_id = request.POST['user_id']
    user = User.objects.get(pk=user_id)
    Tweet.objects.create(text=text, author=user)
    return redirect('/tweets/')


def show_tweets(request):
    tweets = Tweet.objects.all().order_by('date')
    return render(request, 'tweet_list.html', {'tweets': tweets})

