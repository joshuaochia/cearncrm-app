from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ( 
    User, Lead, UserProfile, Agent, Category
    )

admin.site.register(User, UserAdmin)
admin.site.register(Lead)
admin.site.register(UserProfile)
admin.site.register(Agent)
admin.site.register(Category)
