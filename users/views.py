from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views import View

from .forms import UserUpdateForm
from .models import User


class HomeView(ListView):
    users = User.objects.all()
    model = User
    template_name = 'users/home.html'
    context_object_name = 'users'


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        context = {'u_form': UserUpdateForm(instance=request.user)}
        return render(request, 'users/profile.html', context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if not u_form.is_valid():
            return render(request, 'users/profile.html', {'u_form': u_form})

        u_form.save()
        messages.success(request, 'Your account has been updated!')
        return redirect('profile')
