# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse, render, redirect, get_object_or_404, reverse, get_list_or_404 
from .models import Project, Profile
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework.response import Response
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import  ProfileUpdateForm,UserUpdateForm,ProjectForm,RateForm
from django.contrib import messages
import datetime as dt


# Create your views here.
def home(request):
    date = dt.date.today()
    project = Project.objects.all()
    # profile = User.objects.get(username=request.user)
    return render(request,'home.html',locals())
 
@login_required(login_url='/accounts/login')
def upload_project(request):
    if request.method == 'POST':
        uploadform = ProjectForm(request.POST, request.FILES)
        if uploadform.is_valid():
            upload = uploadform.save(commit=False)
            upload.profile = request.user.profile
            upload.save()
            return redirect('home')
    else:
        uploadform = ProjectForm()
    return render(request,'update-project.html',locals())


@login_required(login_url='/accounts/login/')
def profile(request):
    
    return render(request, 'profiles/profile.html')


@login_required(login_url='/accounts/login/')
def updateprofile(request):
    if request.method == 'POST':
        u_form =UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Yoour Account has been updated')
            return redirect('profile')
    else:
        u_form =UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        

    context={
        'u_form':u_form,
        'p_form':p_form

     }
    return render(request, 'updateprofile.html', context)    


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    # permission_classes = (IsAdminOrReadOnly,)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # permission_classes = (IsAdminOrReadOnly,)
@login_required(login_url='/accounts/login')
def rate_project(request,project_id):
    project = Project.objects.get(pk=project_id)
    profile = User.objects.get(username=request.user)
    if request.method == 'POST':
        rateform = RateForm(request.POST, request.FILES)
        print(rateform.errors)
        if rateform.is_valid():
            rating = rateform.save(commit=False)
            rating.project = project
            rating.user = request.user
            rating.save()
            return redirect('vote',project_id)
    else:
        rateform = RateForm()
    return render(request,'rate.html',locals())

def view_rate(request,project_id):
    user = User.objects.get(username=request.user)
    project = Project.objects.get(pk=project_id)
    rate = Rate.objects.filter(project_id=project_id)
    print(rate)
    return render(request,'project.html',locals())
def rate(request):
    profile = User.objects.get(username=request.user)
    return render(request,'rate.html',locals())



@login_required(login_url='/accounts/login/')
def vote(request,project_id):
   try:
       project = Project.objects.get(pk=project_id)
       rate = Rate.objects.filter(project_id=project_id).all()
       print([r.project_id for r in rate])
       rateform = RateForm()
   except DoesNotExist:
       raise Http404()
   return render(request,"project.html", locals())


    