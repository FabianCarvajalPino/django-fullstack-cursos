from django.db import models

# Create your models here.

class CursoManager(models.Manager):
    def basic_validator_curso(self, postData):
        errors = {}
        print(postData)
        if len(postData['name'])<5:
            errors['name'] = "El nombre del curso debe contener al menos 6 caracteres"
        return errors

class DescManager(models.Manager):
    def basic_validator_desc(self, postData):
        errors = {}
        print(postData)
        if len(postData['desc'])<15:
            errors['desc'] = "La descripción debe tener al menos 16 caracteres"
        return errors

class Curso(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CursoManager()

class Description(models.Model):
    curso = models.OneToOneField(Curso, related_name="desc", on_delete=models.CASCADE, primary_key=True)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DescManager()