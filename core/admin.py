# admin.py
from django.contrib import admin
from .models import EmailSubscription,FeedBack

admin.site.register(EmailSubscription)



class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('id', 'feedback')
    search_fields = ('feedback',)
    readonly_fields = ('id',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('feedback',)
        return self.readonly_fields

admin.site.register(FeedBack, FeedBackAdmin)
