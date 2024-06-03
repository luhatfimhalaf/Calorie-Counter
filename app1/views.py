from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import BeratBadan
from .forms import BeratForm

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get (api_url + query,headers = {'X-Api-Key':'9l7JsDHj71UC5enTuOtLCg==rW7peAK9vewX1Ji9'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = 'oops! There was an error'
            print(e)
        return render(request,'home.html',{'api':api})
    else:
        return render(request,'home.html',{'query':'Enter a valid query'})

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are different")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('home')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        email=request.POST.get('email')
        user=authenticate(request,username=username,password=pass1,email=email)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render (request,'login.html')


def LogoutPage(request):
    return render(request,'login.html')

def index(request):
    berat_list = BeratBadan.objects.all()
    return render(request, 'index.html', {'berat_list': berat_list})

def tambah(request):
    if request.method == 'POST':
        form = BeratForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BeratForm()
    return render(request, 'tambah.html', {'form': form})

def edit(request, berat_id):
    berat = BeratBadan.objects.get(pk=berat_id)
    if request.method == 'POST':
        form = BeratForm(request.POST, instance=berat)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BeratForm(instance=berat)
    return render(request, 'edit.html', {'form': form, 'berat_id': berat_id})

def hapus(request, berat_id):
    berat = BeratBadan.objects.get(pk=berat_id)
    berat.delete()
    return redirect('index')

def food(request):
    return render(request,'food.html')
