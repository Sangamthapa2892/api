from django.urls import path
from .views import StudentListCreateAPIView, StudentGetAPIView, LoginAPIView, LogoutApiView #RegisterApiView 

urlpatterns=[
    path('student/',StudentListCreateAPIView.as_view(), name='student'),
    path('student-get/',StudentGetAPIView.as_view(), name='student-get'),
    # path('login/', LoginView.as_view())
    # for token authentication
    # path('register/',RegisterApiView.as_view(), name='register'),
    path('login/',LoginAPIView.as_view(), name='login'),
    path('logout/',LogoutApiView.as_view(), name='logout'),
]