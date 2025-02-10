from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import register_user, login_user, logout_user, get_user_data, update_avatar, update_user, delete_user

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', logout_user, name='logout'),
    path('me/', get_user_data, name='user_data'),
    path('update-avatar/', update_avatar, name='update_avatar'),
    path('update-user/', update_user, name='update_user'),
    path('delete-user/', delete_user, name='delete_user'),
    
]
