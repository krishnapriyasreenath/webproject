from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import authenticate,login



def home(request):
    return render(request,'home.html')
def signup(request):
    return render(request,'signup.html')
def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:  
            if User.objects.filter(username=username).exists(): 
                messages.info(request, 'This username already exists!!!!!!')
        
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                
                print("Successed...")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('/')
    else:
        return render(request,'signup.html')
def loginpage(request):
    return render(request,'login.html') 

def superuser(request):
    return render(request,"admin.html")

#def about(request):
    #if 'uid' in request.session:
        #return render(request,'about.html')    
   # return render(request,'login.html')     

#@login_required(login_url='loginpage')
#def about(request):
  
    #return render(request,'about.html')    
    #return render(request,'login.html')      

def about(request):
    if request.user.is_authenticated:
       return render(request,'about.html')    
    return render(request,'login.html')
    
def log(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
       # request.session["uid"]=user.id
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('superuser')
            else:
                login(request,user)

                auth.login(request,user)
                messages.info(request,f'welcome{username}')
                return redirect('about')
        else:
            messages.info(request,'inavalid username or password')
            return redirect('loginpage')
    return render(request,'login.html')
	


#def logout(request):
     
     #if request.user.is_authenticated:
          #auth.logout(request)
     #return redirect('home')  
       
#@login_required(login_url='loginpage')
#def logout(request):
     #auth.logout(request)
     #return redirect('home')     
   
def logout(request):
     
    request.session["uid"]= ""
    auth.logout(request)
    return redirect('home')     
   