# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

# Create your views here.

# Define a view function for rendering home page
def home_page(request):
    return render(request, 'home.html')


# Define a registration page's view function
def register_page(request):
    # Check if HTTP request method is POST (Form submission)
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user with provided username already exist in database
        user = User.objects.filter(username=username)

        if user.exists():
            #Display an information message if user already exist in database
            messages.info(request, 'User is already taken!')
            # redirect to the registration page
            return redirect('/register/')
    

        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
            )

        # Set the user's password and save the user object
        # user.set_password(password)
        # user.save()


        # Display an success message indicating successful account creation
        messages.success(request, 'Account created Successfully!')
        # redirect to the login page 
        return redirect('/login/')

# Render the registration page (Get request)
    return render(request, 'register.html')



# Define a view function for login page
def login_page(request):
    # Check if the HTTP request method is Post (Form Submmission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        # Check if user with provided username already exists in database
        if not User.objects.filter(username=username).exists():
            #Display an error message if user with provided username does not exist in database
            messages.error(request, 'Invalid Username')
            # redirect to the login page
            return redirect('/login/')
        
        # Authenticate the user with provided username and password
        user = authenticate(username=username, password=password)


        if user is None:
            # Display an error messages if authentication fails
            messages.error(request, 'Invalid Password')
            # Redirect to the login page
            return redirect('/login/')


        else:
            # Login the user and redirect to the home page upon successful login 
            login(request, user)
            # redirect to the home page
            return redirect('/home/')
        
    # render the login page 
    return render(request, 'login.html')







        



