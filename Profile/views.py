from django.shortcuts import redirect, render
from django.contrib import messages
#from django.contrib.auth.decorators import login_required
from Profile.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm



def UserCreation(request):
    user_form = UserCreationForm()
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, ('Your profile was successfully created!'))
            return redirect('login')
        else:
            messages.error(request, ('Please correct the error below.'))
    return render(request, './Registration.html', {
            'form': user_form})

    
