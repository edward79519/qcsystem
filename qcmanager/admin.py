from django.contrib import admin

from qcmanager.models import Project, ProjCategory, Company, Contact
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('psn', 'pname', 'psponsor',)


class ProjCategoryAdmin(admin.ModelAdmin):
    list_display = ('csn', 'cproj', 'cname', 'csponsor',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('cmpsn', 'cmpname', 'cmpsponsor',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('cntname', 'cnttel', 'cntcomp')


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjCategory, ProjCategoryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Contact, ContactAdmin)