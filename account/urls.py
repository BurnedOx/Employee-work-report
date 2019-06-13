from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
    path('', include('master.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.LogIn.as_view(), name='login'),
]