from django.shortcuts import render
from .forms import Student_Registration
from .models import User

# Create your views here.


def add_show(request):
    if request.method == 'POST':
        fm = Student_Registration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = Student_Registration()
    else:
        fm = Student_Registration()
    return render(request, 'enroll/addandshow.html', {'form': fm})
