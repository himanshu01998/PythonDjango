from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import course
from . forms import courseForm, userForm, courseFormEdit, userFormEdit

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    courses = course.objects.all()
    mentors = User.objects.filter(groups=1)
    students = User.objects.filter(groups=2)
    context = {"courses":courses, "mentors":mentors, "students":students,}
    return render(request, 'home.html', context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or Password does not match...')
        except:
            messages.error(request, 'User Not Found....')

    return render(request, 'login.html')

def signupPage(request):
    forms = userForm()
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred")
    context = {"forms":forms,}
    return render(request, 'signup.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def createCourse(request):
    forms = courseForm()
    if request.method == 'POST':
        form = courseForm(request.POST)
        if form.is_valid:
            courses = form.save(commit=False)
            courses.user = request.user
            courses.save()
            return redirect('home')
    context = {"forms":forms,}
    return render(request, 'createcourse.html', context)

def courseDetails(request):
    courses = course.objects.all()
    mentors = User.objects.filter(groups=1)
    students = User.objects.filter(groups=2)
    context = {"courses":courses, "mentors":mentors, "students":students,}
    return render(request, 'course.html', context)

def editCourse(request, pk):
    data = course.objects.get(id=pk)
    forms = courseFormEdit(instance=data)

    if request.method == 'POST':
        form = courseFormEdit(request.POST, instance=data)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {"forms":forms, "data":data}
    return render(request, 'createcourse.html', context)

def applyCourse(request, pk):
    return HttpResponse(pk)
    
@login_required(login_url='login')
def profile(request):
    courses = course.objects.all()
    mentors = User.objects.filter(groups=1)
    students = User.objects.filter(groups=2)
    context = {"courses":courses, "mentors":mentors, "students":students,}
    return render(request, 'profile.html', context)

def students(request):
    courses = course.objects.all()
    mentors = User.objects.filter(groups=1)
    students = User.objects.filter(groups=2)
    context = {"courses":courses, "mentors":mentors, "students":students,}
    return render(request, 'students.html', context)

def mentors(request):
    courses = course.objects.all()
    mentors = User.objects.filter(groups=1)
    students = User.objects.filter(groups=2)
    context = {"courses":courses, "mentors":mentors, "students":students,}
    return render(request, 'mentors.html', context) 

def editUser(request, pk):
    data = User.objects.get(id=pk)
    forms = userFormEdit(instance=data)

    if request.method == 'POST':
        form = userFormEdit(request.POST, instance=data)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {"forms":forms, "data":data}
    return render(request, 'signup.html', context)

def follow(request, pk):
    return HttpResponse(pk)
