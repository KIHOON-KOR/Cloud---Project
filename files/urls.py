from django.urls import path
from .views import FileUploadView, FileListView, FileDeleteView

app_name = "files"

urlpatterns = [
    path("upload/", FileUploadView.as_view(), name="file_upload"),
    path("list/", FileListView.as_view(), name="file_list"),
    path("delete/<int:pk>/", FileDeleteView.as_view(), name="file_delete"),
]