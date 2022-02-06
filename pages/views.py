from django.shortcuts import  redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request,'homePage.html',{})
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            try:
                if not user.birthday == None:
                        redirect('account completion')
                else:
                    redirect('')
            except(AttributeError):
                redirect('home')
                
        else:redirect('home')
    context = {}
    return render()

