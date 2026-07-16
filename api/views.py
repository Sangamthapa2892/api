import time
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Organization
from .serializer import StudentSerializer
from django.db import connection, reset_queries
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.authtoken.models import Token
from config.views import BaseApiView
from django.contrib.auth.models import User
from django.http import JsonResponse
from config.custompermissions import CustomThrottle, NewCustomThrottle
from django.core.cache import cache
from rest_framework.exceptions import Throttled

class StudentListCreateAPIView(BaseApiView):
    throttle_classes = [CustomThrottle, NewCustomThrottle]
        
    def get(self, request):
        try:
            students_data = cache.get("students")
            if not students_data:
                students = Student.objects.all()
                serializer = StudentSerializer(students, many=True)
                students_data = serializer.data
                cache.set("students", students_data, 60)
            return Response({'message':'test successful','data':students_data}, status=200)
        except Exception as e:
            return Response({"message":"Internal server error !!!","data":str(e)}, status=500)   

class StudentGetAPIView(APIView):
    def get(self,request):
        try:
            students_data = cache.get("students")
            if not students_data:
                time.sleep(5)
                students = Student.objects.all()
                serializer = StudentSerializer(students, many=True)
                students_data_from_db= serializer.data
                cache.set("students", students_data_from_db, timeout=10)
                # for deleting cache
                 # cache.delete("students")
                return Response({"message":"Data retrieved successfully from database!!!", "data":students_data_from_db}, status=200)
           
            return Response({"message":"Data retrieved successfully from cache !!!", "data":students_data}, status=200)
        except Exception as e:
            return Response("Internal Server Error")
         

# ================for session authentication==============
# class LoginView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             session_key = request.session.session_key
#         response = Response({
#             "username" : user.username,
#             "cookie": session_key,
#         },status=status.HTTP_200_OK)
#         return response
# from django.middleware.csrf import rotate_token
# from django.contrib.auth import login
# class LoginView(BaseApiView):
#     def get(self,request):
#         username=request.data.get("username")
#         password=request.data.get("password")
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return JsonResponse({"detail": "Logged in"})

# ========================For Token Authentication====================

# class RegisterApiView(BaseApiView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get('password')
#         if not username or password:
#             return Response({
#                 "error":"username or password required"
#             },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         user = User.objects.create_user(username=username, password=password)
#         return Response({
#             "message": "User registered successfully",
#             "username": user.username
#         }, status=status.HTTP_201_CREATED)

class LoginAPIView(BaseApiView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "message":"Login Successful",
                "username":username,
                "token":token.key
            }, status=status.HTTP_200_OK)
        return Response({
            "error":"Invalid Credentials"
        }, status=status.HTTP_400_BAD_REQUEST)
        
class LogoutApiView(BaseApiView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({
            "message":"Logout successful. Token revoked"
        }, status=status.HTTP_200_OK)
    
    
# ==================For JWT Authentication================

