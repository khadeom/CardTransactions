from django.urls import path
from . import views

urlpatterns = [
    path("addcsv/", views.UploadCsv.as_view()),
    path('sort/', views.Sort.as_view())
]
