from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path('', views.faculty_list, name='faculty_list'),
    path('faculty/<int:faculty_id>/departments/', views.department_list, name='department_list'),
    path('department/<int:department_id>/courses/', views.course_list, name='course_list'),
    path('course/<int:course_id>/ebooks/', views.ebook_list, name='ebook_list'),
    path('upload/', views.upload_ebook, name='upload_ebook'),
    path('upload_ebooks_folder/', views.upload_ebooks_folder, name='upload_ebooks_folder'),
    path('done/', views.done, name='done'),
    

]









