from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .forms import RegisterForm , ProfileForm , UpdateProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def RegisterView(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account has created successfully for {username} =)')
        return redirect('login')

    
    context = {
        'form':form
    }

    return render(request,'user/register.html',context)

@login_required
def Profile(request):
    if request.method == 'POST':
        image_form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        user_form = UpdateProfileForm(request.POST,instance=request.user)
        if image_form.is_valid() and user_form.is_valid():
            image_form.save()
            user_form.save()
            messages.success(request,'Profile updated successfully')
            return redirect('home')

    else :
        image_form = ProfileForm(instance=request.user.profile)
        user_form = UpdateProfileForm(instance=request.user)
    
    context = {
        'user_form':user_form,
        'image_form':image_form
    }

    return render(request,'user/profile.html',context)


