"""from django.urls import path, include
#from chat import views as chat_views
from .views import chatPage
from .views import login_user
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Use Django's built-in LogoutView
    path('chatapp/', views.chat_page, name='chaapp'),
    #path('login/', login_user, name='login'),

	# login-section
	#path("", LoginView.as_view(template_name="chat/LoginPage.html"), name="login-user"),
	path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]"""
"""from django.urls import path, include
#from chat import views as chat_views
from .views import chatPage
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path("chat/ ", chatPage, name="chat-page"),

	# login-section
	path("", LoginView.as_view(template_name="chat/LoginPage.html"), name="login-user"),
	path("auth/logout/", LogoutView.as_view(template_name="chat/LoginPage.html"), name="logout-user"),
]"""
"""from django.urls import path, include
from .views import chatPage
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("chat/", chatPage, name="chat-page"),  # Remove the space after "chat/"
    path("", LoginView.as_view(template_name="chat/LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(template_name="chat/LoginPage.html"), name="logout-user"),
]"""

from django.urls import path
from .views import chatPage
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("chat/", chatPage, name="chat-page"),  # Define URL pattern for the chat page
    path("", LoginView.as_view(template_name="chat/LoginPage.html"), name="login-user"),  # Login URL
    path("logout/", LogoutView.as_view(template_name="chat/LoginPage.html"), name="logout-user"),  # Logout URL
]



