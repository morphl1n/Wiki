from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:strname>", views.entry, name="entryname"),
    path("search/", views.query, name="search"),
    path("error101/", views.entry, name="error"),
    path("newpage/", views.NewPage, name="NewPage"),
    path("newlyaddedpage/", views.AddNewPage, name="AddNewPage"),
    path("editpage/", views.EditPage, name="EditPage"),
    path("editedpage/", views.EditedPage, name="EditedPage"),
    path("randompage/", views.RandomPicker, name="RandomPicker")
]
