from django.contrib import admin

from qcmanager.models import Project, ProjCategory, ProjCateSelect, Company, Contact, SubCateSelect
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('psn', 'pname', 'psponsor',)


class ProjCateSelectAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProjCategoryAdmin(admin.ModelAdmin):
    list_display = ('csn', 'cproj', 'cname', 'csponsor',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('cmpsn', 'cmpname', 'cmpsponsor',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('cntname', 'cnttel', 'cntcomp',)


class SubCateSelectAdmin(admin.ModelAdmin):
    list_display = ('prntcat', 'name',)



admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjCateSelect, ProjCateSelectAdmin)
admin.site.register(ProjCategory, ProjCategoryAdmin)
admin.site.register(SubCateSelect, SubCateSelectAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Contact, ContactAdmin)
