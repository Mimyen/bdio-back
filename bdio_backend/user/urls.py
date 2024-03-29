from django.urls import path, include
from .views import (
    CreateUserView,
    ProfileUserView,
    ConfirmUserView,
    TutorDescriptionView,
    ProfileImageView,
    CheckUserPasswordView,
    DeleteUserView,
)
from django_rest_passwordreset.urls import reset_password_request_token, reset_password_confirm

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('delete/', DeleteUserView.as_view(), name='delete'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('confirm_user/',ConfirmUserView.as_view(), name='confirm_user'),
    path('tutor/decription/', TutorDescriptionView.as_view(), name='tutor_description'),
    path('profile_image/',ProfileImageView.as_view(), name='profile_image'),
    path('check_password/', CheckUserPasswordView.as_view(), name='check_password'),
]
