from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Core_index'),
    path('register/', views.user_signup, name='Register'),
    path('changepwd/', views.user_change_pwd, name='User_chgpwd'),
    path('update/', views.user_update_profile, name='User_update'),
]