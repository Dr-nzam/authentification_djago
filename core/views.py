from django.shortcuts import redirect, render
from django.contrib import messages
from .form import UserForm

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

def index(request):
   return render(request, 'core/index.html')