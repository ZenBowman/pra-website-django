from django.shortcuts import render
from django.http import HttpResponse
from models import BlogPost, HeaderElement
from django.http import HttpResponseRedirect

from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

def thanks(request):
    return render(request, 'blog/thanks.html')
    
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("thanks/")
    else:
        form = RegisterForm()
        return render(request, 'blog/register.html', { 'form': form })

# Create your views here.
def index(request):
    blog_list = BlogPost.objects.order_by('-pub_date')
    header_list = HeaderElement.objects.order_by('name')
    context = {'blog_list': blog_list,
               'header_list': header_list}
    return render(request, 'blog/index.html', context)
    
