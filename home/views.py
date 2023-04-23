from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login



def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        fname=request.POST.get('fname')
        username=request.POST.get('id')
        city=request.POST.get('city')
        state=request.POST.get('state')
        mobile=request.POST.get('mob')
        row1=Contact(name=name,fname=fname,username=username,city=city,state=state,mobile=mobile)
        row1.save()
        messages.success(request, ' Your Data has been Submitted Succesffully.')
    return render(request,'contact.html')
def service  (request):
    return render(request,'service.html')
def support  (request):
    return render(request,'support.html')
def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username,password)
        if user is not None:
            login(request,user)
            messages.success(request, ' You have Succesffully Logged In !!! Welcome to your Own Personalized Webisite !!!!!!!!!!!!!')
            return redirect('/')
         # A backend authenticated the credentials
        else:
            messages.warning(request,"Please Enter Valid Username And Password Combination !!")
            return render(request,'login.html')
            # No backend authenticated the credentials
    return render(request,'login.html')
        

def logoutuser(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')
