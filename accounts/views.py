from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm, ProfileUpdateForm
from .models import ApplicantProfile

def register_view(request):
    if request.user.is_authenticated:
        return redirect('applicant_dashboard')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        ApplicantProfile.objects.create(user=user, phone=form.cleaned_data['phone'])
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('applicant_dashboard')
    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        if user.is_staff:
            return redirect('admin_dashboard')
        return redirect('applicant_dashboard')
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    profile, _ = ApplicantProfile.objects.get_or_create(user=request.user)
    form = ProfileUpdateForm(request.POST or None, instance=profile)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile})