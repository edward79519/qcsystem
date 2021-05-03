from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from core.models import Employee, Department


# Register your models here.
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dname',)


# register User model
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# register Department model
admin.site.register(Department, DepartmentAdmin)
