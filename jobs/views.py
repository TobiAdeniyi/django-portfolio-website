from django.shortcuts import render, get_object_or_404
from .models import Job


def homepage(request):
    jobs = Job.objects.all()
    response = {'jobs': jobs}
    return render(request, 'jobs/home.html', response)


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    response = {'job': job_detail}
    return render(request, 'jobs/detail.html', response)
