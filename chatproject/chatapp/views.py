from django.shortcuts import render, redirect
#from django.contrib.auth import logout

def chatPage(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect("login_user")
	context = {}
	return render(request,"chat/chatPage.html",context)


"""def logout_view(request):
	logout(request)
	return redirect ("chat/login-user")"""
"""from django.shortcuts import render, redirect
from .models import Message

def chatPage(request):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)

def create_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            # Assuming the user is logged in and authenticated
            message = Message.objects.create(user=request.user, content=content)
            # Optionally, you can perform additional operations here
    return redirect('chat-page')

"""