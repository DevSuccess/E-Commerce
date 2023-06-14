from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

from . import views
from . import forms

app_name = 'product'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),
    path('category-title/<val>/', views.CategoryTitle.as_view(), name='category-title'),
    path('product-detail/<int:id>/', views.ProductDetail.as_view(), name='product-detail'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('update-address/<int:id>/', views.UpdateAddress.as_view(), name='update-address'),

    # login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customer-registration'),
    path('accounts/login/', auth_view.LoginView.as_view(
        template_name='app/login.html',
        authentication_form=forms.LoginForm), name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(
        template_name='app/password_reset.html',
        form_class=forms.MyPasswordResetForm), name='password-reset'),
    path('password-change/', auth_view.PasswordChangeView.as_view(
        template_name='app/change_password.html',
        form_class=forms.MyPasswordChangeForm,
        success_url='/password-change-done'
    ), name='password-change'),
    path('password-change-done/', auth_view.PasswordChangeDoneView.as_view(
        template_name='app/password_change_done.html'
    ), name='password-change-done')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
