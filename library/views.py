from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Faculty, Department, Course, E_Book
from .forms import EBookUploadForm ,CourseForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def faculty_list(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('q')
        faculties = Faculty.objects.filter(name__icontains=query) if query else Faculty.objects.all()

        paginator = Paginator(faculties, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        faculty_data = [
            {
                'id': faculty.id,
                'name': faculty.name,
                'image_url': faculty.image_url,
                'num_departments': faculty.num_departments
            } for faculty in page_obj
        ]

        return JsonResponse({
            'faculties': faculty_data,
            'current_page': page_obj.number,
            'has_previous': page_obj.has_previous(),
            'has_next': page_obj.has_next()
        })
    else:
        faculties = Faculty.objects.all()
        return render(request, 'lib/faculty_list.html', {'faculties': faculties})

def department_list(request, faculty_id):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    departments = Department.objects.filter(faculty=faculty)

    paginator = Paginator(departments, 6)
    page_number = request.GET.get('page')
    try:
        departments = paginator.page(page_number)
    except PageNotAnInteger:
        departments = paginator.page(1)
    except EmptyPage:
        departments = paginator.page(paginator.num_pages)

    return render(request, 'lib/department_list.html', {'faculty': faculty, 'departments': departments})


def course_list(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    courses = Course.objects.filter(department=department)

    paginator = Paginator(courses, 6)  # Change 6 to the number of courses you want per page
    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    return render(request, 'lib/course_list.html', {'department': department, 'courses': courses, 'department_id': department_id})



def create_course(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.department = department
            course.save()
            return redirect('library:course_list', department_id=department_id)
    else:
        form = CourseForm()
    return render(request, 'lib/create_course.html', {'form': form, 'department': department,})

from django.core.paginator import Paginator

def ebook_list(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    ebooks = E_Book.objects.filter(course=course)
    paginator = Paginator(ebooks, 8)  # Show 10 ebooks per page
    page_number = request.GET.get('page')
    ebooks_page = paginator.get_page(page_number)
    return render(request, 'lib/ebook_list.html', {'course': course, 'ebooks': ebooks_page})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.validators import FileExtensionValidator
from .forms import EBookUploadForm
from .models import E_Book, Course


@login_required
def ebook_upload(request, course_id=None):
    course = None
    if course_id:
        course = get_object_or_404(Course, pk=course_id)
    department = course.department if course else None
    faculty = department.faculty if department else None

    if request.method == 'POST':
        form = EBookUploadForm(request.POST, request.FILES)
        course_code = request.POST.get('course_code')

        if form.is_valid():
            file = request.FILES['file']
            valid_extensions = ['pdf', 'epub', 'mobi', 'txt', 'ppt', 'pptx', 'doc', 'docx']
            ext = file.name.split('.')[-1].lower()
            if ext in valid_extensions:
                ebook = E_Book(file=file, user=request.user)
                if course_code:
                    try:
                        course = Course.objects.get(course_code=course_code)
                    except Course.DoesNotExist:
                        course = None

                if course:
                    ebook.course = course
                    ebook.save()
                else:
                    return render(request, 'lib/ebook_upload.html', {
                        'form': form,
                        'faculty': faculty,
                        'department': department,
                        'course': course,
                        'error_message': 'No course found with the entered course code.'
                    })
                return redirect('library:upload_successful', course_id=course_id)

    else:
        form = EBookUploadForm()

    return render(request, 'lib/ebook_upload.html', {
        'form': form,
        'faculty': faculty,
        'department': department,
        'course': course
    })

def upload_successful(request, course_id):
    context = {
        'course_id': course_id,
    }
    return render(request, 'lib/upload_successful.html', context)

def download_ebook(request, ebook_id):
    ebook = get_object_or_404(E_Book, pk=ebook_id)
    response = HttpResponse(ebook.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{ebook.title}.pdf"'
    return response