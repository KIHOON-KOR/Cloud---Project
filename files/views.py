from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.files.storage import default_storage
from .models import File
from .serializers import FileSerializer

class FileUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return Response({"error": "파일이 필요합니다."}, status=400)

        file_instance = File.objects.create(
            user=request.user,
            file=uploaded_file,
            name=uploaded_file.name,
            size=uploaded_file.size,
        )

        return Response(FileSerializer(file_instance).data, status=201)


class FileListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        files = File.objects.filter(user=request.user).order_by("-created_at")
        return Response(FileSerializer(files, many=True).data)


class FileDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        file_obj = File.objects.filter(id=pk, user=request.user).first()

        if not file_obj:
            return Response({"error": "파일이 없습니다."}, status=404)

        file_obj.file.delete()  # 실제 파일 삭제
        file_obj.delete()       # DB 삭제
        return Response({"message": "삭제 완료!"})
