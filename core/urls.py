"""using for create path configuration"""
from django.urls import path
from core.views import RegisterView, ContactView, AboutView, LoginView, LogoutView, BlogView, BlogDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('contact/', ContactView, name='contact'),
    path('about/', AboutView, name='about'),
    path('', BlogView.as_view(), name='blog'),
    path('blog_details/<slug:slug>', BlogDetailView.as_view(), name='blog-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
