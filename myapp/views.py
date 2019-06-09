from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views import generic

from .forms import MyTableForm

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def home(request):
    return render(request,'index.html')



class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def addData(request):
    form = MyTableForm()
    if(request.method == 'POST'):
        form = MyTableForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return render(request,'success.html')

    return render(request,'addData.html',{'form':form,})



def page2(request):
    return render(request,'page2.html')

def page3(request):
    return render(request,'page3.html')
