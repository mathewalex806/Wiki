from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("Random",views.Random, name="Random"),
    path("wiki/create/", views.create, name="create"),
    path("wiki/search", views.search, name="search"),
    path("edit",views.edit,name="edit"),
    path("save_edit/", views.save_edit, name= "save_edit"),
    path("wiki/<str:title>/", views.title, name="title"),
]
