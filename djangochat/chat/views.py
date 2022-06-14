from django.shortcuts import render, redirect
from django.contrib.auth import login 
from .forms import SignUpForm

# Create your views here.

def frontpage(request):
    return render(request, "chat/frontpage.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')

    else:
        form = SignUpForm()

    return render(request, 'chat/signup.html', {'form': form})