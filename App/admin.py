from django.contrib import admin

from App import models

# Register your models here.

admin.site.register(models.LoginView)
admin.site.register(models.Member)
admin.site.register(models.Trainer)
admin.site.register(models.WorkOutPlan)
admin.site.register(models.selectStatus)
admin.site.register(models.Community)
