from django.contrib import admin
from django.contrib.auth.views import LoginView

from core import models, forms

admin.site.site_header = "Admin Management System"
admin.site.index_title = "Welcome To Admin Management"
admin.site.site_title = "Primary Control Hub"


admin.site.register(models.User)
admin.site.register(models.Role)
admin.site.register(models.Skill)

admin.site.login =  LoginView.as_view(
             template_name='core/login.html',
             authentication_form=forms.LoginForm,
             extra_context={ 'title': 'Log in',}
         )
