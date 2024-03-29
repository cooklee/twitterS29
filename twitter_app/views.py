from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.views import View

from twitter_app.models import User, Tweet, Group, URGENT


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
    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('/login/')
    if request.method == 'GET':
        return render(request, 'add_tweet.html', {'urgent':URGENT})
    text = request.POST['text']
    urgent = request.POST['urgent']
    user = User.objects.get(pk=user_id)
    Tweet.objects.create(text=text, author=user, urgent=urgent)
    return redirect('/tweets/')

class AddGroupView(View):
    def get(self, request):
        user_id = request.session.get('user_id')
        if user_id is None:
            return redirect('/login/')
        return render(request, 'add_group.html')

    def post(self, request):
        user_id = request.session.get('user_id')
        if user_id is None:
            return redirect('/login/')
        name = request.POST['name']
        user = User.objects.get(pk=user_id)
        Group.objects.create(name=name, owner=user)
        return redirect('/groups/')

class ListGroupView(View):
    def get(self, request):
        groups = Group.objects.all()
        return render(request, 'groups.html', {'groups':groups})


def show_tweets(request):
    search_text = request.GET.get('text', '')
    username = request.GET.get('username', '')
    urgent = request.GET.get('urgent', '0')
    tweets = Tweet.objects.filter(text__icontains=search_text).order_by('date')
    tweets = tweets.filter(author__username__icontains=username)
    if urgent != '0':
        tweets = tweets.filter(urgent=urgent)
    return render(request, 'tweet_list.html', {'tweets': tweets, 'URGENT':URGENT})


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            request.session['user_id'] = user.id
            return render(request, 'login.html',{'message':'logowanie udane'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'message':'nie poprawne dane'})


class LogoutView(View):

    def get(self, request):
        if 'user_id' in request.session:
            del request.session['user_id']
        return redirect('/')

class DelUserView(View):

    def get(self, request, id):
        return render(request, 'del_user_form.html',
                      {'user':User.objects.get(pk=id)})

    def post(self, request, id):
        if request.POST['potwierdzenie'] == 'tak':
            u = User.objects.get(pk=id)
            u.delete()
        return redirect('/')


class SetCookieLanguage(View):

    def get(self, request):
        return render(request, 'set_language.html')

    def post(self, request):
        lang = request.POST['ln']
        http_response = redirect('/')
        http_response.set_cookie('ln', lang)
        return http_response


class JoinGroupView(View):

    def get(self, request, id):
        user_id = request.session.get('user_id')
        if user_id is None:
            return redirect('/')
        g = Group.objects.get(id=id)
        u = User.objects.get(pk=user_id)
        g.users.add(u)
        return redirect('/groups/')

