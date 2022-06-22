from users.forms import CustomUserCreationForm, LoginForm
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm
from users.backends import MyAuthBackend
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib import messages

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "authentication/register.html"

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if request.method == "POST":

            if form.is_valid():
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password")
                user = MyAuthBackend.authenticate(email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/")
                else:
                    messages.info(request, "Invalid User")
            else:
                 messages.info(request, "Invalid Info")

    else:
         form = LoginForm()
    context = {
            'form':form
        }
    return render(request, 'authentication/login.html', context)