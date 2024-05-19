from django.contrib import admin
from .models import Category, NickName, Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'google_link', 'nick_name_display', 'categories_list')

    def nick_name_display(self, obj):
        return obj.nick_name.name if obj.nick_name else '-'
    nick_name_display.short_description = 'Nickname'

    def categories_list(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    categories_list.short_description = 'Categories'

admin.site.register(Category)
admin.site.register(NickName)
admin.site.register(Location, LocationAdmin)
