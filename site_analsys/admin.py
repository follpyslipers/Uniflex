from django.contrib import admin
from django.utils import timezone
from django.db.models import Count
from .models import Visitor

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'user_agent', 'visit_date', 'page_visited', 'visit_time', 'session_key')
    list_filter = ('visit_date', 'page_visited')
    search_fields = ('ip_address', 'user_agent', 'page_visited', 'session_key')
    change_list_template = 'admin/visitors_change_list.html'
    date_hierarchy = 'visit_date'

    def changelist_view(self, request, extra_context=None):
        today = timezone.now().date()
        visitors_today = Visitor.objects.filter(visit_date=today).count()
        engagement = Visitor.objects.filter(visit_date=today).values('page_visited').annotate(visits=Count('id')).order_by('-visits')

        extra_context = extra_context or {}
        extra_context['visitors_today'] = visitors_today
        extra_context['engagement'] = engagement
        return super().changelist_view(request, extra_context=extra_context)
