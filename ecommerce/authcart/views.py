from django.shortcuts import render,redirect

# Create your views here.
def signup(request):
    if(request.method=="POST"):
        print("it is post request")
    return render(request,"signup.html")

def handlelogin(request):
    return render(request,"login.html")

def handlelogout(request):
    return redirect('/auth/login')