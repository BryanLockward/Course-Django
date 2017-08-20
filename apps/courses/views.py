import re
from .models import Course
from django.contrib import messages
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def validate(new_course):
    error=""
    for key in new_course:
        if len(new_course[key])<2:
            error="All fields must contain more than two characters"

    return error


def create(request):
    new_course={}

    for key,value in request.POST.items():
        if key!="csrfmiddlewaretoken":
            new_course[key]=value

    message=validate(new_course)
    print new_course

    if len(message)>1:
        messages.error(request, message)
        return redirect('/')

    Course.objects.create(
        name=new_course["name"],
        descript=new_course["descript"],
    )
    return redirect("/")

def confirm(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, 'courses/show.html', context)

def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')
