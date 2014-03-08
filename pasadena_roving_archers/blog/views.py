from django.shortcuts import render
from django.http import HttpResponse
from models import BlogPost, HeaderElement, ArcheryClass, ClassRegistration
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django import forms

def renderWithHeader(request, template, dict):
    if request.user:
        dict["username"] = request.user.username
    header_list = HeaderElement.objects.order_by('order')
    dict["header_list"] = header_list
    return render(request, template, dict)

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")

def classes(request):
    classes = ArcheryClass.objects.order_by('date')
    return renderWithHeader(request, 'blog/classes.html', {'classes' : classes })

def thanks(request):
    return renderWithHeader(request, 'blog/thanks.html')

def user_exists(request):
    form = RegisterForm()
    return renderWithHeader(request, 'blog/register.html', {'form' : form, 'userexists': True})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data["email"]
            if (len(User.objects.filter(email = new_email)) > 0):
                return HttpResponseRedirect("userexists/")
            user = User.objects.create_user(new_email, new_email, form.cleaned_data["password"])
            user.save()
            return HttpResponseRedirect("thanks/")
    else:
        form = RegisterForm()
        return renderWithHeader(request, 'blog/register.html', { 'form': form, 'userexists': False })

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            pwd = form.cleaned_data["password"]
            user = authenticate(username=email, password=pwd)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/")
            return HttpResponseRedirect("/blog/login_failed/")
    else:
        form = LoginForm()
        return renderWithHeader(request, 'blog/login.html', { 'form': form })


# Create your views here.
def index(request):
    blog_list = BlogPost.objects.order_by('-pub_date')
    context = {'blog_list': blog_list}
    return renderWithHeader(request, 'blog/index.html', context)

@login_required
def signup(request):
    class_id = request.GET.get("class_id")
    class_by_id = ArcheryClass.objects.filter(id = class_id)[0]
    if request.user:
        ClassRegistration.objects.create_class(class_by_id, request.user)
    return HttpResponseRedirect("/blog/classes/")
