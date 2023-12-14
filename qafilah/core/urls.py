from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('signout', auth_views.LogoutView.as_view(template_name='core/base.html'), name='signout'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmation/',views.confirmation, name='confirmation')
]