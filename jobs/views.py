from django.shortcuts import render
from .models import Job

# Create your views here.


def homepage(request):
    jobs = Job.objects.all()
    response = {'jobs': jobs}
    return render(request, 'jobs/home.html', response)
