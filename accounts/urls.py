from django.urls import path
from accounts.views import relatives
from accounts.views.account import account_update, activate, manage_accounts,activation_sent, confirm_email, custom_login, custom_logout, general, register, user_details
from accounts.views.passwords import password_change, password_reset_request, password_reset_sent, passwordResetConfirm

app_name = "accounts"
urlpatterns = [
    path("accounts/login", custom_login, name="login"),
    path('accounts/logout', custom_logout, name='logout'),
    path("accounts/register", register, name="register"),
    path('accounts/details/<str:username>', user_details, name="user-details"),
    path('accounts/register/success', activation_sent, name='success'),
    path('accounts/activate/<uidb64>/<token>', activate, name='activate'),
    path('accounts/confirm/email/<uidb64>/<token>', confirm_email, name='confirm-email'),
    path("accounts/password/reset", password_reset_request, name="password-reset"),
    path('accounts/password/success', password_reset_sent, name='password-reset-sent'),
    path('accounts/password/reset/<uidb64>/<token>', passwordResetConfirm, name='password-reset-confirm'),
    path("accounts/password/reset", password_reset_request, name="password-reset"),
    path('accounts/password/success', password_reset_sent, name='password-reset-sent'),
    path('accounts/password/reset/<uidb64>/<token>', passwordResetConfirm, name='password-reset-confirm'),

    path('dashboard/accounts/update/profile', account_update, name="profile-update"),
    path('dashboard/accounts/update/contact', general, name="contact-update"),
    path('dashboard/accounts/update/password', password_change, name="password-update"),

    path('dashboard/accounts/all', manage_accounts, name="manage-accounts"),
    path('dashboard/relatives', relatives.all_relatives, name="all-relatives"),
    path('dashboard/relatives/api', relatives.relatives_api, name="relatives-api"),
    path('dashboard/relatives/details/<uuid:id>', relatives.relative, name="relative"),
    path('dashboard/relative/update/<uuid:id>', relatives.update_relative, name="update-relative"),
    path('dashboard/relative/delete/<uuid:id>', relatives.delete_relative, name="delete-relative"),
    path('dashboard/relative/create', relatives.create_relative, name="create-relative"),
]
