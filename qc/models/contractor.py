from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ContractBase(models.Model):
    editor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_rltd',
        related_query_name='%(app_label)s_%(class)ss',
    )
    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    isvalid = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Company(ContractBase):
    cmpname = models.CharField(max_length=50)
    cmpsn = models.CharField(max_length=10)
    cmpsponsor = models.ForeignKey(
        'Contact',
        on_delete=models.PROTECT,
        related_name='cmpsponsor',
        blank=True,
        null=True,
    )
    cmptel = models.CharField(max_length=20)
    cmpfax = models.CharField(max_length=20, blank=True, null=True)
    cmpaddr = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.cmpsn + '_' + self.cmpname


class Contact(ContractBase):
    name = models.CharField(max_length=20)
    comp = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='contcomp',
        blank=True,
        null=True,
    )
    telprim = models.CharField(max_length=20)
    telscnd = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        if self.comp:
            return self.name + "_" + self.comp.cmpname
        else:
            return self.name
