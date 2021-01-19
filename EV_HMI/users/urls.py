from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CompanyDetailView, UserDetailView, CompanyDeleteView, UserDeleteView

urlpatterns = []

profile_urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/settings/', views.profile_edit, name='profile-edit'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/password_change/',
         auth_views.PasswordChangeView.as_view(template_name='users/password_change.html',
                                               extra_context={'sidebar': 'Settings'}), name='password-change'),
    path('profile/password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html',
                                                   extra_context={'sidebar': 'Settings'}), name='password_change_done'),
]

urlpatterns += profile_urlpatterns

user_urlpatterns = [
    path('user/create', views.create_user, name='create-user'),
    path('register/<int:pk>/', views.register_employee, name='register-employee'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/edit/', views.user_edit, name='user-edit'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]

urlpatterns += user_urlpatterns

company_urlpatterns = [
    path('company/create/', views.create_company, name='create-company'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('company/<int:pk>/edit/', views.company_edit, name='company-edit'),
    path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company-delete'),
]

urlpatterns += company_urlpatterns
