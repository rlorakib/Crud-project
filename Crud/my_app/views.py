from django.shortcuts import render
from my_app import forms
from my_app.models import student
# Create your views here.

def index(request):
    student_list = student.objects.order_by('first_name')
    diction = {'title':'Home','student_list':student_list}
    return render(request, 'first_project/index.html', context=diction)



def students(request):
    form = forms.StudentForm()

    if request.method == 'POST':
        form = forms.StudentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title':'Student Form', 'student_form':form}
    return render(request, 'first_project/student_form.html', context=diction)


def student_info(request,student_id):
    student_info = student.objects.get(pk=student_id)
    diction = {'student_info':student_info}
    return render(request,'first_project/student_info.html', context=diction)


def student_update(request,x_id):
    student_info = student.objects.get(pk=x_id)
    form = forms.StudentForm(instance=student_info)

    if request.method == 'POST':
        form = forms.StudentForm( request.POST, instance=student_info )
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
    diction = {'form':form}
    return render(request, 'first_project/student_update.html', context=diction)



def student_delete(request,x_id):
    students = student.objects.get(pk=x_id).delete()
    diction = {'students':students, 'delete_message':'Delete Done'}
    return render(request,'first_project/student_delete.html', context=diction)