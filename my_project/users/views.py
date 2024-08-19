from django.shortcuts import render, redirect
# rejestracja 
# login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.

def register_view(request):

  if request.method == "POST":
    form = UserCreationForm(request.POST)

    if form.is_valid():
      login(request, form.save())
      return redirect("posts:list")
    else:
      print(form.errors)  # Wydrukuj błędy w konsoli
    # Jeśli formularz nie jest poprawny, renderuj ten sam formularz z błędami
      return render(request, 'register.html', { "form": form })
    
  else:
    form = UserCreationForm()

    return render(request, 'register.html', { "form": form })


def login_view(request):

  if request.method == "POST":
    form = AuthenticationForm(data=request.POST)

    if form.is_valid():
        
      # login here needs a request and user value get by this method
      login(request, form.get_user())
      return redirect("posts:list")
    
    else:
      print(form.errors)  # Wydrukuj błędy w konsoli
      # Jeśli formularz nie jest poprawny, renderuj ten sam formularz z błędami
      return render(request, 'login.html', { "form": form })

  else:
    form = AuthenticationForm()

    return render(request, 'login.html', { "form": form })

