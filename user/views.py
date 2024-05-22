from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import User
from .forms import UserRegisterForm

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, f"You are already logged in.")
        return redirect("account:account")
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            matric_number = form.cleaned_data.get("matric_number")
            messages.success(request, f"Hey {matric_number}, your account was created successfully.")
            user = authenticate(matric_number=form.cleaned_data['matric_number'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect("E_libary:ebook_list")
        else:
            # If the form is not valid, display the errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = UserRegisterForm()
    
    context = {
        "form": form
    }
    return render(request, "Auth/sign-up.html", context)


from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import User

def LoginView(request):
    if request.method == "POST":
        matric_number = request.POST.get("matric_number")
        password = request.POST.get("password")

        try:
            user = User.objects.get(matric_number=matric_number)
            user = authenticate(request, matric_number=matric_number, password=password)
            
            if user is not None:  # if there is a user
                login(request, user)
                if user.is_class_rep:
                    messages.success(request, "You are logged in as a class representative.")
                    return redirect("E_libary:ebook_list")
                else:
                    messages.success(request, "You are logged in.")
                    return redirect("E_libary:ebook_list")
            else:
                messages.warning(request, "Username or password does not exist")
                return redirect("user:sign-in")
        except User.DoesNotExist:
            messages.warning(request, "User does not exist")

    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("E_libary:ebook_list")
        
    return render(request, "Auth/sign-in.html")




def logoutView(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("user:sign-in")