from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    psn = models.CharField(max_length=4)
    pname = models.CharField(max_length=20)
    ploc_county = models.CharField(max_length=20)
    ploc_area = models.CharField(max_length=20)
    ploc_secnum_list = models.CharField(max_length=20, null=True, blank=True)
    psponsor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='proj_sponsor')
    pstatrtime = models.DateField()
    pendtime = models.DateField(null=True, blank=True)
    paddtime = models.DateTimeField(auto_now_add=True)
    pupdatetime = models.DateTimeField(auto_now=True)
    peditor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='proj_editor')

    def __str__(self):
        return self.psn + self.pname


class ProjCateSelect(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCateSelect(models.Model):
    prntcat = models.ForeignKey(ProjCateSelect, on_delete=models.PROTECT, related_name='parent_cat')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProjCategory(models.Model):
    csn = models.CharField(max_length=4)
    cproj = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='cate_proj')
    cname = models.ForeignKey(ProjCateSelect, on_delete=models.PROTECT, related_name='cat_select_name')
    csponsor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='cate_sponsor')
    cstatrtime = models.DateField()
    cendtime = models.DateField(null=True, blank=True)
    caddtime = models.DateTimeField(auto_now_add=True)
    cupdatetime = models.DateTimeField(auto_now=True)
    ceditor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='cate_editor')

    def __str__(self):
        return self.csn + self.cname.name


class Company(models.Model):
    cmpname = models.CharField(max_length=50)
    cmpsn = models.CharField(max_length=8, unique=True)
    cmpsponsor = models.CharField(max_length=20)
    cmptel = models.CharField(max_length=20)
    cmpfax = models.CharField(max_length=20, null=True, blank=True)
    cmpaddr = models.CharField(max_length=100)

    def __str__(self):
        return self.cmpname + self.cmpsn


class Contact(models.Model):
    cntname = models.CharField(max_length=20)
    cntcomp = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='cnt_comp', blank=True, null=True)
    cnttel = models.CharField(max_length=20)
    cntemail = models.EmailField()

    def __str__(self):
        return self.cntname + self.cntcomp.cmpname
