from django.shortcuts import render, redirect
from users.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }
        return render(request, 'users/register.html', context=context)

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password1=form.cleaned_data.get('password1')
                )
                return redirect('/users/register/')
            else:
                form.add_error('password1', 'Чет не так, соболезную')

        return render(request, 'users/register.html', context={'form': form})


def login_view(request):
    if request.method == "GET":
        context = {
            'context': LoginForm
        }

        return render(request, 'users/login.html', context=context)

    if request.method == "GET":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            """authenticate user"""
            user = authenticate(request, username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))

            if user:
                login(request, user)
                return redirect('/products/')
            else:
                form.add_error('username', 'lox')

        return render(request, 'users/login.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('/posts/')
