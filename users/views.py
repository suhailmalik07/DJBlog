from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class RegisterView(View):
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        form_class = UserRegisterForm()
        return render(request, self.template_name, {'form': form_class})

    def post(self, request, *args, **kwargs):
        form_class = UserRegisterForm(request.POST)
        if form_class.is_valid():
            form_class.save()
            messages.success(
                request, f"Your account has beed created now you can Login!")
            return redirect('login')
        return render(request, self.template_name, {'form': form_class})


class ProfileView(LoginRequiredMixin, View):
    template_name = 'users/profile.html'

    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your Profile updated!")
            return redirect('profile')
        return render(request, self.template_name, context)
