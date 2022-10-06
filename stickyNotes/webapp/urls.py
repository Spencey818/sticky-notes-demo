from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('register', views.register_request, name='Register'),
    path('login', views.login_request, name='Login'),
    path('logout', views.logout_request, name='Logout'),
    path('note/<str:userID>/<str:noteID>', views.viewNote, name='View Note')
]