from django.db import models
from django.contrib.auth.models import User
from .contractor import Contact
from django.utils.translation import gettext_lazy as _


class SelfCheckBase(models.Model):
    sponsor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_spnsr',
        related_query_name='%(app_label)s_%(class)sspnsr',
    )
    starttime = models.DateField()
    endtime = models.DateField(blank=True, null=True)
    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    editor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_editor',
        related_query_name='%(app_label)s_%(class)seditor',
    )
    remark = models.CharField(max_length=200, blank=True, null=True)
    isvalid = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Project(SelfCheckBase):
    sn = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=20)
    loc_county = models.CharField(max_length=20)
    loc_area = models.CharField(max_length=20)

    def __str__(self):
        return self.sn + '_' + self.name


class CategorySelectName(models.Model):
    sn = models.CharField(max_length=3)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.sn + "_" + self.name


class Category(SelfCheckBase):
    name = models.ForeignKey(
        CategorySelectName,
        on_delete=models.PROTECT,
    )
    proj = models.ForeignKey(Project, on_delete=models.PROTECT)

    def __str__(self):
        return self.name.sn + '_' + self.name.name


class SubCateSelect(models.Model):
    cate = models.ForeignKey(
        CategorySelectName,
        on_delete=models.PROTECT,
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.cate.name + '_' + self.name


class TimingSelect(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id).zfill(2) + '_' + self.name


class WorkList(SelfCheckBase):
    cate = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcate = models.ForeignKey(SubCateSelect, on_delete=models.PROTECT)
    timing = models.ForeignKey(
        TimingSelect,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=200)
    contractor = models.ForeignKey(
        Contact,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.cate.name.name + '_' + self.name


class QuestionCategory(models.Model):
    subcate = models.ForeignKey(
        SubCateSelect,
        on_delete=models.PROTECT,
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}_{}".format(self.subcate.name, self.name)


class Question(models.Model):

    class QType(models.IntegerChoices):
        SINGLECHOICE_TYPE = 0, _('單選題')
        MULTICHOICE_TYPE = 1, _('複選題')
        TEXT_TYPE = 2, _('填空題')
        IMAGE_TYPE = 3, _('圖片題')
        FILE_TYPE = 4, _('檔案題')

    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    isvalid = models.BooleanField(default=True)
    editor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_editor',
    )
    worklist = models.ForeignKey(
        WorkList,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_worklist',
    )
    category = models.ForeignKey(
        QuestionCategory,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_cate',
    )
    ordering = models.IntegerField()
    title = models.CharField(max_length=200)
    abstract = models.CharField(max_length=200, blank=True, null=True)
    rank = models.IntegerField()
    method = models.CharField(max_length=100, blank=True, null=True)
    goodimg = models.ImageField(upload_to='uploads/selfcheck/%Y/%m/%d/', blank=True, null=True)
    badimg = models.ImageField(upload_to='uploads/selfcheck/%Y/%m/%d/', blank=True, null=True)
    improvement = models.CharField(max_length=100, blank=True, null=True)
    type = models.IntegerField(choices=QType.choices, default=QType.SINGLECHOICE_TYPE)
    is_required = models.BooleanField(default=True)

    def __str__(self):
        return self.category.name + "_" + self.title

    class Meta:
        unique_together = [['id', 'ordering']]


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.PROTECT,
        related_name="q_choice",
    )
    desc = models.CharField(max_length=100)
    multi = models.BooleanField(default=False)

    def __str__(self):
        return self.desc


class Task(models.Model):
    worklist = models.ForeignKey(
        WorkList,
        on_delete=models.PROTECT,
        related_name='tasks'
    )
    sponsor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='sponsortasks'
    )
    sched_time = models.DateField()
    cmplt_time = models.DateField(blank=True, null=True)
    count = models.IntegerField()
    isvalid = models.BooleanField(default=True)
    is_filled = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_check = models.BooleanField(default=False)
    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    editor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='editortasks',
    )

    def __str__(self):
        return self.worklist.name + self.sponsor.get_full_name()


class AnswerBase(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_task',
    )
    addtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    editor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_editor'
    )

    class Meta:
        abstract = True


class AnsSingle(AnswerBase):
    choice = models.ForeignKey(
        Choice,
        on_delete=models.PROTECT,
        related_name='single_choice'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.PROTECT,
        related_name='single_choice_question'
    )

    def __str__(self):
        return '{}_{}_{}'.format(self.question.title, self.choice.desc, self.editor.username)


class AnsFilled(AnswerBase):
    question = models.ForeignKey(
        Question,
        on_delete=models.PROTECT,
        related_name="filled_ans"
    )
    ans = models.CharField(max_length=50)

    def __str__(self):
        return '{}_{}'.format(self.question.title, self.ans)
