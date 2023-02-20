from django.shortcuts import render,redirect
from django.contrib import messages
from . import forms
from JMC.forms import Feedback
from .models import *


# Create your views here.
def home(request):
    return render(request,"jmc/home.html")

def feedback(request):
    form = forms.Feedback()
    if request.method=='POST':
        form=forms.Feedback(request.POST)
        if form.is_valid():
            messages.success(request,"Feedback Submitted, Thank You")
            return redirect(request,'jmc/home.html')
    return render(request,"jmc/feedback.html",{'form':form})