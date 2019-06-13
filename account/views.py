from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import generic
from .forms import userForm
from django.conf import settings

# Create your views here.
class SignUp(generic.View):
    form_class = userForm
    template_name = 'account/sign-up.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name, {'form': form})

class LogIn(generic.View):
    form_class = userForm
    template_name = 'account/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name, {'form': form})