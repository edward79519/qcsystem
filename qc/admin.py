from django.contrib import admin
from .models import (
    Contact, Company, Project, Category, CategorySelectName, SubCateSelect, TimingSelect,
    WorkList, Question, QuestionCategory, Choice, Task, AnsSingle,
)

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comp')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'cmpname', 'cmpsponsor', 'cmpsn')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'sn', 'name', 'sponsor', 'loc_county')


class CateSelectAdmin(admin.ModelAdmin):
    list_display = ('sn', 'name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'proj', 'name', 'sponsor')


class SubCateSelectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class TimingSelectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class WorkListAdmin(admin.ModelAdmin):
    list_display = ('id', 'cate', 'subcate', 'timing', 'name', 'sponsor')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'worklist', 'category', 'ordering', 'title', 'type')


class QuestCateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'desc')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'worklist', 'sched_time', 'sponsor')


class AnsSingleAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice', 'editor')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(CategorySelectName, CateSelectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCateSelect, SubCateSelectAdmin)
admin.site.register(TimingSelect, TimingSelectAdmin)
admin.site.register(WorkList, WorkListAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionCategory, QuestCateAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(AnsSingle, AnsSingleAdmin)
