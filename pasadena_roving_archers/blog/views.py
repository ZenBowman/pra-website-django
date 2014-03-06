from django.shortcuts import render
from django.http import HttpResponse
from models import BlogPost, HeaderElement

from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    
def register(request):
    form = RegisterForm()
    return render(request, 'blog/register.html', { 'form': form })

# Create your views here.
def index(request):
    blog_list = BlogPost.objects.order_by('-pub_date')
    header_list = HeaderElement.objects.order_by('name')
    context = {'blog_list': blog_list,
               'header_list': header_list}
    return render(request, 'blog/index.html', context)
    
