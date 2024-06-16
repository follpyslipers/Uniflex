from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path('', views.faculty_list, name='faculty_list'),
    path('faculty/<int:faculty_id>/departments/', views.department_list, name='department_list'),
    # path('department/<int:department_id>/courses/', views.course_list, name='course_list'),
    path('department/<int:department_id>/courses/', views.course_list, name='course_list'),
    path('department/<int:department_id>/create_course/', views.create_course, name='create_course'),
    path('courses/<int:course_id>/ebooks/', views.ebook_list, name='ebook_list'),
    path('upload/<int:course_id>/', views.ebook_upload, name='upload_ebook'),

]









