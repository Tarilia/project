from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)
from django.urls import path, reverse_lazy

from dogblog.users.views import (CreateUserView, LoginUserView, LogoutUserView,
                                 ProfileUserView, DeleteUserView,
                                 PasswordUserChange)

urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create_users"),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
    path('password-change/', PasswordUserChange.as_view(),
         name="password_change"),
    path('password-reset/', PasswordResetView.as_view(
        template_name="users/password_reset_form.html",
        email_template_name="users/password_reset_email.html",
        success_url=reverse_lazy("password_reset_done")),
        name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name="users/password_reset_done.html"),
        name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name="users/password_reset_confirm.html",
        success_url=reverse_lazy("password_reset_complete")),
        name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name="users/password_reset_complete.html"),
        name='password_reset_complete'),
    path("<int:pk>/delete/", DeleteUserView.as_view(), name="delete_users"),
]
