from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos),
    path('create', views.create),
    path('cursos/delete/<int:id>', views.delete),
    path('cursos/destroy/<int:id>', views.destroy)
]