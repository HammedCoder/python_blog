"To import login" 
from django.contrib.auth import views as auth_views
include its url in the admin urls
path('login/', auth_views.LoginView.as_views(template_name='users/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_views(template_name='users/logout.html'), name='logout'),