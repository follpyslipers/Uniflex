from django.shortcuts import render, get_object_or_404
from .models import Faculty, Department, Course, E_Book
from django.http import JsonResponse
from .models import Faculty

def done (request):
    return render(request, 'done.html')


from django.http import JsonResponse
from django.shortcuts import render
from .models import Faculty

def faculty_list(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Check if it's an AJAX request for live filtering
        query = request.GET.get('q')
        faculties = Faculty.objects.filter(name__icontains=query) if query else Faculty.objects.all()
        faculty_data = [
            {
                'id': faculty.id,
                'name': faculty.name,
                'image_url': faculty.image_url,  # Use the image_url property
                'num_departments': faculty.num_departments  # Use the num_departments property
            } for faculty in faculties
        ]
        return JsonResponse({'faculties': faculty_data})
    else:  # Render the initial page
        faculties = Faculty.objects.all()
        return render(request, 'lib/faculty_list.html', {'faculties': faculties})






def department_list(request, faculty_id):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    departments = Department.objects.filter(faculty=faculty)
    return render(request, 'lib/department_list.html', {'faculty': faculty, 'departments': departments})



def course_list(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    courses = Course.objects.filter(department=department)
    return render(request, 'lib/course_list.html', {'department': department, 'courses': courses})



def ebook_list(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    ebooks = E_Book.objects.filter(course=course)
    return render(request, 'lib/ebook_list.html', {'course': course, 'ebooks': ebooks})


from django.shortcuts import render, redirect
from .forms import EBookForm

def upload_ebook(request):
    if request.method == 'POST':
        form = EBookForm(request.POST, request.FILES)
        if form.is_valid():
            ebook = form.save(commit=False)
            ebook.user = request.user  # Assuming you have a user field in your E_Book model
            ebook.save()
            return redirect('library:done')  # Redirect to the ebook list page or another appropriate view
    else:
        form = EBookForm()
    return render(request, 'upload_ebook.html', {'form': form})




###################################################################################################################################################################

import os
from django.shortcuts import render
from django.core.files import File
from .models import Faculty, Department, Course, E_Book

def upload_ebooks_folder(request):
    if request.method == 'POST':
        # Specify the directory where the e-books are located
        ebooks_directory = "C:Users/USER/Desktop/Uniabujaflex/uniabuja_app/Malik pdfs"
        

        # Create a Faculty and Department with 'Untitled' names if they don't exist
        faculty, _ = Faculty.objects.get_or_create(name='Untitled Faculty')
        department, _ = Department.objects.get_or_create(name='Untitled Department', faculty=faculty)

        # Iterate through the files in the specified directory
        for filename in os.listdir(ebooks_directory):
            # Assuming the file names are unique or can be uniquely identified
            title, ext = os.path.splitext(filename)
            if ext.lower() in ['.pdf', '.epub', '.mobi', '.txt', '.ppt', '.pptx', '.doc', '.docx']:
                # Create a Course for each e-book with a unique course code
                course, _ = Course.objects.get_or_create(course_code=f"CODE_{title}", department=department)
                
                # Create an E_Book instance and assign properties
                ebook = E_Book.objects.create(
                    title=title,
                    description="Description goes here",
                    course=course,
                    status=E_Book.APPROVED,  # Assuming all e-books are approved
                )
                
                # Open and upload the file to the E_Book instance
                with open(os.path.join(ebooks_directory, filename), 'rb') as file:
                    ebook.file.save(filename, File(file), save=True)

        return render(request, 'upload_success.html')  # Render a success page after uploading
    else:
        return render(request, 'upload_form.html')  # Render a form for uploading e-books

