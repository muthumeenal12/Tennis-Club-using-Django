import django
from django.urls import path
from . import views

urlpatterns = [
    path('members/',views.members,name = 'members'),
    path('',views.home , name = 'home'),
    path("join/", views.join, name="join"),
    path("join/thanks/", views.join_thanks, name="join_thanks"),
    path("contact/", views.contact, name="contact"),
    
    #Authentication URLS
    path('signup/', views.signup, name='signup'),
    path('login/', django.contrib.auth.views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
