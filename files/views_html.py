from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import File

# 파일 업로드
@login_required
def file_upload_page(request):
    message = None

    if request.method == "POST":
        uploaded = request.FILES.get("file")
        if uploaded:
            File.objects.create(
                user=request.user,
                file=uploaded,
                name=uploaded.name,
                size=uploaded.size
            )
            message = "업로드 완료!"
        else:
            message = "파일을 선택해주세요."

    return render(request, "files/upload.html", {"message": message})


# 파일 목록
@login_required
def file_list_page(request):
    files = File.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "files/list.html", {"files": files})


# 삭제
@login_required
def file_delete_page(request, pk):
    file = File.objects.filter(id=pk, user=request.user).first()
    if file:
        file.file.delete()
        file.delete()
    return redirect("html_files:file_list_page")
