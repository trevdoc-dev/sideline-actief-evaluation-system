"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from userauth import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("admin/", admin.site.urls),
    path("login/", views.login_page, name="login"),
    path("edit/<int:_id>/update", views.edit_page, name="edit_page"),
    path("user_page/", views.user_page, name="user_page"),
    path("evaluation/", views.evaluation_page, name="evaluation_page"),
    path("analytics/", views.analytics_page, name="analytics_page"),

    # CRUD operations ...
    path("questions/", views.question_list, name="question_list"),
    path("questions/create/", views.create_question, name="create_question"),
    path("questions/<int:_id>/update/", views.update_question, name="update_question"),
    path("questions/<int:_id>/delete/", views.delete_question, name="delete_question"),
]
