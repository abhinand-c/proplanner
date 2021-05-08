from django.contrib import admin

from core import models


admin.site.site_header = "Admin Management System"
admin.site.index_title = "Welcome To Admin Management"
admin.site.site_title = "Primary Control Hub"


admin.site.register(models.User)
admin.site.register(models.Role)
admin.site.register(models.Skill)
