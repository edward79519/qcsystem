from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from core.models import Employee, Department, County, Area, Section, Land


# Register your models here.
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dname',)


class CountyAdmin(admin.ModelAdmin):
    list_display = ('sn', 'name')


class AreaAdmin(admin.ModelAdmin):
    list_display = ('sn', 'name', 'county')


class SectionAdmin(admin.ModelAdmin):
    list_display = ('sn', 'name', 'area', 'office')


class LandAdmin(admin.ModelAdmin):
    list_display = ('sn', 'section')


# register User model
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# register Department model
admin.site.register(Department, DepartmentAdmin)

admin.site.register(County, CountyAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Land, LandAdmin)
