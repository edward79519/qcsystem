from django.db import models
from django.contrib.auth.models import User
from .basic import Project, Contact
from django.utils.translation import gettext_lazy as _


# 檢查時機(可調整)表格
class TimingChoice(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# 基本資料
class Base(models.Model):
    # 表頭
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    contractor = models.ForeignKey(Contact, on_delete=models.PROTECT)
    chkuser = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_chkuser',
    )
    chkloc = models.CharField(max_length=100)
    chktime = models.DateField()
    timing = models.ForeignKey(TimingChoice, on_delete=models.PROTECT)
    # 編輯紀錄
    addtime = models.DateTimeField(auto_now_add=True)
    edittime = models.DateTimeField(auto_now=True)
    editor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_editor',
    )

    class Meta:
        abstract = True


class SlfChkStandIn(Base):
    class Rank(models.IntegerChoices):
        NORMAL = 1
        MEDIUM = 2
        HIGH = 3

    sn = models.CharField(max_length=20)
    worksn = models.CharField(max_length=20)
    amount = models.IntegerField()
    stncrtf = models.BooleanField()
    stncrtf_rk = models.IntegerField(choices=Rank.choices)
    stnoutfit = models.BooleanField()
    stnoutfit_rk = models.IntegerField(choices=Rank.choices)
    stnrust = models.BooleanField()
    stnrust_rk = models.IntegerField(choices=Rank.choices)
    prlnrust = models.BooleanField()
    prlnrust_rk = models.IntegerField(choices=Rank.choices)
    prlndfm = models.BooleanField()
    prlndfm_rk = models.IntegerField(choices=Rank.choices)

    def __str__(self):
        return self.worksn + '_' + self.sn

    def score(self):
        score = self.stncrtf * self.stncrtf_rk \
                + self.stnoutfit * self.stnoutfit_rk \
                + self.stnrust * self.stnrust_rk \
                + self.prlndfm * self.prlndfm_rk \
                + self.prlnrust * self.prlnrust_rk

        return score

    def total_score(self):
        total = self.stncrtf_rk + self.stnoutfit_rk + self.stnrust_rk + self.prlnrust_rk + self.prlndfm_rk

        return total