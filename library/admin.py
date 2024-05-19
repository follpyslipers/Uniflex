from django.contrib import admin
from .models import Faculty, Department, Course, E_Book

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty',)
    list_filter = ('faculty',)
    search_fields = ('name',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'title', 'department',)
    list_filter = ('department',)
    search_fields = ('course_code', 'title',)

class E_BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'uploaded_at', 'status',)
    list_filter = ('status', 'course__department__faculty',)
    search_fields = ('title', 'description', 'course__course_code',)
    readonly_fields = ('uploaded_at',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(E_Book, E_BookAdmin)
