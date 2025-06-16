from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms import *
from app.models import Student 


# Create your views here.

# def student_view(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             reg = Student(name=name,email=email,password=password)
#             reg.save()
#             form = StudentForm()
#     else:
#         form = StudentForm()

#     data = Student.objects.all()

#     return render(request,'index.html',{'form':form,'data':data})

def student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Data Enter Successfully!')
            return redirect('student')
    else:
        form = StudentForm()

    data = Student.objects.all()

    return render(request,'index.html',{'form':form,'data':data})

def update_view(request,id):
    if request.method == 'POST':
        pd = Student.objects.get(pk=id)
        form = StudentForm(request.POST,instance=pd)
        if form.is_valid():
            form.save()
    else:
        pd = Student.objects.get(pk=id)
        form = StudentForm(instance=pd)

    return render(request,'update.html',{'form':form})


def delete_view(request,id):
    if request.method == "POST":
        d = Student.objects.get(pk=id)
        d.delete()
        messages.success(request,'Student Data Delete Successfully!')
        return redirect('student')

