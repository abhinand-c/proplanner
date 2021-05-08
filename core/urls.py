from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, forms

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            template_name='core/login.html',
            redirect_authenticated_user=True,
            authentication_form=forms.LoginForm,
            extra_context={'title': 'Log-in'}
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),

]
