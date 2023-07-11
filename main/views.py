from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from . models import*
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request, 'index.html')



def register(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password,email=email)
        messages.success(request, 'Message alert: You have already register!')
        return redirect('login')
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Message alert: You are wellcome to voting system!')
            return redirect('vote')
        else:
            return redirect('login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')




@login_required(login_url='login')
def page_vote(request):
    candidates = Candidate.objects.all()
    if request.method == 'POST':
        candidate_id = request.POST['candidate']
        if Vote.objects.filter(user=request.user).exists():
            messages.success(request, 'Message alert: You have already voted !')
            return redirect('vote')
    if request.method == 'POST':
        candidate_id = request.POST['candidate']
        
        Vote.objects.create(user=request.user, candidate_id=candidate_id)
        messages.success(request, 'Message alert: Successfully voting!')
        return redirect('results')
    return render(request, 'vote.html', {'candidates': candidates})

@login_required(login_url='login')
def results(request):
    votes = Vote.objects.filter(user=request.user)
    return render(request, 'results.html', {'votes': votes})
  