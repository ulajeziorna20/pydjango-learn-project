from django.shortcuts import render, redirect
# rejestracja
from django.contrib.auth.forms import UserCreationForm 


# Create your views here.

def register_view(request):

  if request.method == "POST":
    form = UserCreationForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect("posts:list")
    else:
      print(form.errors)  # Wydrukuj błędy w konsoli
    # Jeśli formularz nie jest poprawny, renderuj ten sam formularz z błędami
      return render(request, 'register.html', { "form": form })
    
  else:
    form = UserCreationForm()

    return render(request, 'register.html', { "form": form })

