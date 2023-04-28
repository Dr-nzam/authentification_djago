from django.shortcuts import redirect, render
from django.contrib import messages
from .form import UserForm
from django.contrib.auth import authenticate, login


def register(request):
    form = UserForm()
    if request.method =='POST':
        form = UserForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "votre compte a ete bien creer")
            return redirect(index)
    context = {'form':form}
    return render(request, 'core/register.html',context)

def connexion(request):
    if request.method == 'POST':
        nameUser= request.POST['nameuser'] 
        password= request.POST['pass'] 
        user = authenticate(request, username=nameUser, password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request, 'welcome back')
            return redirect(index)
    return render(request, 'core/login.html')

def index(request):
   return render(request, 'core/index.html')