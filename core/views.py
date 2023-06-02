from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import SignupForm, UpdateProfile

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

def profile_view(request):
    # form = UpdateProfile(instance=request.user)
    username = request.user.username
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    return render(request, 'core/profile.html',{
        #"form": form
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    })

#https://stackoverflow.com/questions/9957371/how-to-update-user-object-without-creating-new-one
def profile_update(request):
    if request.method == "POST":
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            #return HttpResponseRedirect(reverse('profile'))
            return render(request, 'core/profile_update.html', {
            "form": form,
            "message": "Profile updated"
        })
    else:
        form = UpdateProfile(instance=request.user)
        return render(request, 'core/profile_update.html', {
            "form": form,
        })
