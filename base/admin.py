from django.contrib import admin

# Register your models here.
from .models import Food,Comment,Type

admin.site.register(Type)
admin.site.register(Food)
admin.site.register(Comment)