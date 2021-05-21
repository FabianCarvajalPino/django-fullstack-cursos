from django.shortcuts import render, redirect
from .models import Curso, Description
from django.contrib import messages

# Create your views here.
def cursos(request):
    curso = Curso.objects.all()
    context = {
        'cursos': curso
    }
    return render(request, 'courses.html', context)

def create(request):
    errors_curso = Curso.objects.basic_validator_curso(request.POST)
    errors_desc = Description.objects.basic_validator_desc(request.POST)
    if len(errors_curso) > 0 or len(errors_desc) > 0:
        for key, value in errors_curso.items():
            messages.error(request, value)
        for key, value in errors_desc.items():
            messages.error(request, value)
    else:
        c = Curso.objects.create(
            name=request.POST['name']
        )
        Description.objects.create(
            desc=request.POST['desc'],
            curso=c
        )
    return redirect('/')


def delete(request, id):
    curso_to_delete = Curso.objects.get(id=id)
    context = {
        'curso': curso_to_delete
    }
    return render(request, 'delete.html', context)

def destroy(request, id):
    curso_to_delete = Curso.objects.get(id=id)
    curso_to_delete.delete()
    return redirect("/")