from django.contrib import admin
from django.contrib.auth.models import User

# Optionally customize admin registration
admin.site.unregister(User)
admin.site.register(User)