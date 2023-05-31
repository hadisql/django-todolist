from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .forms import SignupForm

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        "form": form
    })

def logout_view(request):
    logout(request)
    return render(request, 'core/index.html', {
        "message": "Logged Out"
    })
