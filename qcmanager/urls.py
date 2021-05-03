from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Qc_index'),
    path('category/', views.category, name='Cate_list'),
    path('category/workslist/', views.works, name='Work_list'),
    path('catecory/workslist/arrange/', views.arng, name='Arng_list'),
    path('catecory/workslist/arrange/add/', views.arng_add, name='Arng_add'),
]