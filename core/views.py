from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Contact, PortfolioUpdate, Theme, Skill
from django.core import validators
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


from .forms import RegistrationForm, PortfolioUpdateForm
# Create your views here.



def index(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            contact = Contact(name=name, email=email, subject=subject, message=message, date=datetime.today())
            contact.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('/index')
        else:
            messages.success(request, 'Something went wrong!')
            return redirect('/index')


    if request.user.username:
        data = PortfolioUpdate.objects.get(user=request.user)
        context ={
            'title': 'Home',
            'data': data
        }
        return render(request, 'core/index.html', context)

    context ={
            'title': 'Home',
    }
    return render(request, 'core/index.html', context)



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('portfolio')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('portfolio')
            else:
                messages.info(request, 'Credentials mitchmath!')

        context ={
            'title': 'Login',
        }
        return render(request, 'core/login.html', context)



def signup(request):
    if request.user.is_authenticated:
        return redirect('portfolio')
    else:
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                userP = User.objects.get(username=username)
                pu = PortfolioUpdate(user=userP)
                pu.save()
                messages.success(request, username)
                return redirect('signup')

        
        context ={
            'title': 'Signup',
            'form': form,
        }
        return render(request, 'core/signup.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def portfolio(request):
    data = PortfolioUpdate.objects.get(user=request.user)
    context ={
        'title': 'Portfolio',
        'data': data
    }
    return render(request, 'core/portfolio.html', context)


@login_required(login_url='login')
def portfolio_edit(request):
    if request.method == 'POST':
        user = PortfolioUpdate.objects.get(user=request.user)
        form = PortfolioUpdateForm(instance=user)

        sk = request.POST.getlist('skills')
        th = request.POST.get('theme')

        form = PortfolioUpdateForm(request.POST, request.FILES, instance=user)
        
        if form.is_valid():
            form.save()

            ptheme = Theme.objects.get(name=th)
            ptheme.popularity += 1
            ptheme.save()

            upport = PortfolioUpdate.objects.get(user=request.user)
            upport.skills = sk
            upport.theme = th
            upport.save()
            messages.success(request, 'Your portfolio has been updated.')
            return redirect('portfolio-edit')
        else:
            messages.error(request, 'Something went wrong.')
    else:
        user = PortfolioUpdate.objects.get(user=request.user)
        form = PortfolioUpdateForm(instance=user)
        themedata = Theme.objects.all()
        skdata = Skill.objects.all()
        data = PortfolioUpdate.objects.get(user=request.user)
        context ={
            'title': 'Edit portfolio',
            'form': form,
            'themedata': themedata,
            'skdata': skdata,
            'user': user,
            'data': data,
        }
        return render(request, 'core/portfolio-edit.html', context)



def portfolio_public(request, username):
    count = User.objects.filter(username=username).count()
    
    if count:
        user = User.objects.get(username=username)
        data = PortfolioUpdate.objects.get(user=user)
        theme = Theme.objects.get(name=data.theme)
        skdata = Skill.objects.all()
        if data.name and  data.title and data.about and data.phone and data.email and data.city and data.country and data.facebook and data.uni and data.uni_subject and data.clg and data.clg_group and  data.clg_result and data.clg_passing and data.theme and data.image:
            context ={
                'data': data,
                'skdata':skdata,
            }
            pty = PortfolioUpdate.objects.get(user=request.user)
            pty.popularity += 1
            pty.save()
            return render(request, 'core/theme/'+ theme.html, context)
        else:
            context ={
                'username': username,
            }
            return render(request, 'core/not-completed.html', context)
    else:
        return render(request,'core/404.html')
        

@login_required(login_url='login')
def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password has been changed.')
            return HttpResponseRedirect('/change-pass/')
        else:
            messages.error(request, 'Something went wrong.')
            return HttpResponseRedirect('/change-pass/')
    else:
        form = PasswordChangeForm(user=request.user)
        data = PortfolioUpdate.objects.get(user=request.user)
        context = {
            'title':'Change Password',
            'form':form, 
            'data':data
        }
    return render(request, 'core/change-pass.html', context)



# error 404
def error_404(request, exception):
    data = {}
    return render(request,'core/404.html', data)
        
