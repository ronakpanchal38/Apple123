from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(AppleModel)
class AppleAdmin(admin.ModelAdmin):
    list_display = ('fname','lname','email','password','cpass','phone')