from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.student_index, name="students.index"),
    path("students/create/", views.student_create, name="students.create"),
    path("students/update/", views.student_update, name="students.update"),
    path("students/edit/<int:id>/", views.student_edit, name="students.edit"),
    path("students/show/<int:id>/", views.student_show, name="students.show"),
    path("students/delete/<int:id>/", views.student_delete, name="students.delete"),

    # user
    path("users/register/", views.user_register, name="users.register"),
    path("users/login/", views.user_login, name="users.login"),
]