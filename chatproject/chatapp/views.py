"""from django.shortcuts import render, redirect
#from django.contrib.auth import logout

def chatPage(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect("login_user")
	context = {}
	return render(request,"chat/chatPage.html",context)
"""
# chat/views.py
from django.shortcuts import render, redirect
from .models import Message

def chatPage(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(content=content)
            return redirect('chat-page')
    
    return render(request, 'chat/chatPage.html')



"""

{'messages': messages}
"""

