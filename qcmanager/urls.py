from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Qc_index'),
    path('proj/', views.project, name='Pj_list'),
    path('proj/<int:p_id>/', views.proj_detail, name='Pj_detail'),
    path('slfchkstanin/<int:chk_id>/', views.slfchkstandin_detail, name='SlfChkStandIn_detail'),
    path('category/<int:cate_id>/', views.cate_detail, name='Cate_detail'),
    path('category/', views.category, name='Cate_list'),
    path('category/workslist/', views.works, name='Work_list'),
    path('catecory/workslist/arrange/', views.arng, name='Arng_list'),
    path('catecory/workslist/arrange/add/', views.arng_add, name='Arng_add'),
]