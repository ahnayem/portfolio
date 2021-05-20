from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signup, name='signup'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-edit/', views.portfolio_edit, name='portfolio-edit'),
    path('logout/', views.logoutPage, name='logout'),
    path('change-pass/', views.change_pass, name='change-pass'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='core/resetpass/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='core/resetpass/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='core/resetpass/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='core/resetpass/password_reset_done.html'), name='password_reset_complete'),

    path('<str:username>/', views.portfolio_public, name='portfolio-public'),
]

# error 404
handler404 = 'core.views.error_404'