from django.contrib import admin
from .models import New, Comment
# Register your models here.
admin.site.register(Comment)
admin.site.register(New)