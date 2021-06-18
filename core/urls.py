from django.urls import path
from . import views, ajax

urlpatterns = [
    path('', views.index, name='Core_index'),
    path('register/', views.user_signup, name='Register'),
    path('changepwd/', views.user_change_pwd, name='User_chgpwd'),
    path('update/', views.user_update_profile, name='User_update'),
    path('land/', views.land_list, name='Land_List'),
    path('land/addland/', views.land_add, name='Land_Add'),
    path('ajax/getarea/', ajax.getArea),
    path('ajax/getsection/', ajax.getSection),
    path('ajax/getlandgps/', ajax.getLandGPS),
]
