from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Qc_Index"),
    path('project/<int:proj_id>/', views.proj_detail, name="Proj_Detail"),
    path('project/<int:proj_id>/update/', views.proj_update, name="Proj_Update"),
    path('project/<int:proj_id>/addcate/', views.cate_add, name="Cate_Add"),
    path('project/add/', views.proj_add, name="Proj_Add"),
    path('category/selectlist/', views.cate_select_list, name="CateSelect_List"),
    path('category/<int:cate_id>/', views.cate_detail, name="Cate_Detail"),
    path('category/<int:cate_id>/update/', views.cate_update, name="Cate_Update"),
    path('category/<int:cate_id>/addwklst/', views.worklist_add, name="WkLst_Add"),
    path('category/<int:cate_id>/selectlist/', views.worklist_cate_select_add, name="WkLstCat_List"),
    path('worklist/<int:wk_id>/', views.worklist_detail, name='WkLst_detail'),
    path('worklist/<int:wk_id>/update/', views.worklist_update, name="WkLst_Update"),
    path('worklist/timinglist/', views.timing_list, name="Timing_List"),
    path('question/<int:quest_id>/', views.question_detail, name='Question_detail'),
    path('question/<int:quest_id>/<int:choice_id>/delete/', views.choice_delete, name='Choice_Delete'),
    path('task/<int:task_id>/fill/', views.task_fill, name='Task_Fill'),
    path('task/<int:task_id>/', views.task_detail, name='Task_Detail'),
    path('contractor/', views.contractor_index, name='Contra_Index'),
    path('contact/add/', views.contact_add, name='Contact_Add'),
    path('contact/<int:cont_id>', views.contact_detail, name='Contact_Detail'),
    path('company/addnew/', views.comp_add_jump, name='Comp_Add_Jump'),
    path('company/', views.comp_list, name='Comp_List'),
    path('company/<int:cmp_id>/', views.comp_detail, name='Comp_Detail'),
]

