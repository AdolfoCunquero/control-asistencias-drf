from django.urls import path
from user.api.views import RegisterView, UserView, RolView, AllUserListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('auth/me/', UserView.as_view()),
    path('rol/', RolView.as_view()),
    path('users/', AllUserListView.as_view()),
]