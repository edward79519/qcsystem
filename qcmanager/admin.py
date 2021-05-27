from django.contrib import admin

from qcmanager.models import (
    Project, ProjCategory, ProjCateSelect, Company, Contact, SubCateSelect,
    SlfChkStandIn, TimingChoice,
)
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


class SlfChkStandInAdmin(admin.ModelAdmin):
    list_display = ('id', 'sn', 'worksn', 'chkuser', 'amount',)


class TimingChoiceAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Project, ProjectAdmin,)
admin.site.register(ProjCateSelect, ProjCateSelectAdmin,)
admin.site.register(ProjCategory, ProjCategoryAdmin,)
admin.site.register(SubCateSelect, SubCateSelectAdmin,)
admin.site.register(Company, CompanyAdmin,)
admin.site.register(Contact, ContactAdmin,)
admin.site.register(SlfChkStandIn, SlfChkStandInAdmin,)
admin.site.register(TimingChoice, TimingChoiceAdmin,)
