from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import UserRegistrationAPIView, UserLoginAPIView, UserListAPIView, RoleListCreateAPIView, RoleDetailAPIView
from . import views

urlpatterns = [
    path('',views.Registration),
    path('registration-data/',views.Registration_Data),
    path('login/',views.login),
    path('login-data/',views.login_data),
    path('table/',views.table),
    path('update/<int:id>',views.update,name='edit'),
    path('update-data/',views.update_data),
    path('delete/<int:id>',views.delete,name='delete'),
    path('roles/',views.roles),
    path('roles-data/',views.roles_data),
    path('api/register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('api/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('api/users/', UserListAPIView.as_view(), name='user-list'),
    path('api/roles/', RoleListCreateAPIView.as_view(), name='role-list-create'),
    path('api/roles/<int:pk>/', RoleDetailAPIView.as_view(), name='role-detail'),

]
