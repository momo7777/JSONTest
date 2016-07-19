from django.contrib import admin
from models import stuffs_sort
# Register your models here.

class stuffs_sortAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image')

admin.site.register(stuffs_sort , stuffs_sortAdmin)

