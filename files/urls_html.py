from django.urls import path
from .views_html import file_upload_page, file_list_page, file_delete_page

app_name = "html_files"

urlpatterns = [
    path("", file_list_page, name="file_list_page"),
    path("upload/", file_upload_page, name="file_upload_page"),
    path("delete/<int:pk>/", file_delete_page, name="file_delete_page"),
]
