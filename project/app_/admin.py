from django.contrib import admin
from .models import Category


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
# ,CategoryAdmin


admin.site.register(Category)
