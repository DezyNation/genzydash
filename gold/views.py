from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html');

def managementcontrols(request):
    return render(request, 'managementcontrols.html');

def grades(request):
    return render(request, 'grades.html');

def sections(request):
    return render(request, 'sections.html');

def subjects(request):
    return render(request, 'subjects.html');

def users(request):
    return render(request, 'users.html');

def userdata(request):
    return render(request, 'userdata.html');

def examsmanage(request):
    return render(request, 'examsmanage.html');

def lessonplanouter(request):
    return render(request, 'lessonplanouter.html');

def lessonplaninner(request):
    return render(request, 'lessonplaninner.html');

def collections(request):
    return render(request, 'collections.html');

def payouts(request):
    return render(request, 'payouts.html');
