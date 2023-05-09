from django.urls import path

from . import views

app_name = "book_outlet"

urlpatterns = [
    path("", views.index, name="index-page"),
    path("<slug:slug>/", views.book_detail, name="book-detail"),
]
