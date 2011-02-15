from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def vista_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message

    else:
        # Return an 'invalid login' error message.

def logout_view(request):
    logout(request)
    # Redirect to a success page
    return HttpResponseRedirect('/login/?next=%s' % request.path)

