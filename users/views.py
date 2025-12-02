from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer

# 회원가입
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 성공!"}, status=201)
        return Response(serializer.errors, status=400)

# 로그인(SimpleJWT 기본 TokenObtainPairView 사용)
class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

# 로그아웃 (Refresh Token 블랙리스트 등록)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "로그아웃 완료!"}, status=205)
        except Exception:
            return Response({"error": "유효하지 않은 refresh token"}, status=400)
