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
from .forms import  ProfileUpdateForm,UserUpdateForm
from django.contrib import messages

# Create your views here.
def home (request):
    projects = Project.objects.all()
    return render(request, 'home.html', {"projects": projects})   


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
