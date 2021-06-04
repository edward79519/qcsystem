from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="Qc_Index"),
    path('project/<int:proj_id>/', views.proj_detail, name="Proj_Detail"),
    path('project/<int:proj_id>/update/', views.proj_update, name="Proj_Update"),
    path('project/<int:proj_id>/addcate/', views.cate_add, name="Cate_Add"),
    path('project/add/', views.proj_add, name="Proj_Add"),
    path('category/<int:cate_id>/', views.cate_detail, name="Cate_Detail"),
    path('category/<int:cate_id>/update/', views.cate_update, name="Cate_Update"),
    path('category/<int:cate_id>/addwklst/', views.worklist_add, name="WkLst_Add"),
    path('worklist/<int:wk_id>/', views.worklist_detail, name='WkLst_detail'),
    path('worklist/<int:wk_id>/update/', views.worklist_update, name="WkLst_Update"),
    path('question/<int:quest_id>/', views.question_detail, name='Question_detail'),
    path('question/<int:quest_id>/<int:choice_id>/delete/', views.choice_delete, name='Choice_Delete'),
    path('task/<int:task_id>/fill/', views.task_fill, name='Task_Fill'),
    path('task/<int:task_id>/', views.task_detail, name='Task_Detail'),
]

