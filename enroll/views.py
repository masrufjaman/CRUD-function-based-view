from django.shortcuts import render
from .forms import Student_Registration

# Create your views here.


def add_show(request):
    if request.method == 'POST':
        fm = Student_Registration(request.POST)
    else:
        fm = Student_Registration()
    return render(request, 'enroll/addandshow.html', {'form':fm})
