from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm


# Home View
def home(request):
    # return HttpResponse("Hello World!")
    return render(request, 'webapp/index.html')

# Register View
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            # return redirect('')

    context = {'form': form}

    return render(request, 'webapp/register.html', context)
