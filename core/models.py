from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Department(models.Model):
    dname = models.CharField(max_length=20)

    def __str__(self):
        return self.dname


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=20, null=True, blank=True)
    ext = models.CharField(max_length=5, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="Dept_name")


class County(models.Model):
    sn = models.CharField(max_length=1, unique=True)
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ['sn']

    def __str__(self):
        return "{}_{}".format(self.sn, self.name)


class Area(models.Model):
    sn = models.CharField(max_length=3)
    county = models.ForeignKey(
        County,
        on_delete=models.PROTECT,
        related_name="area",
    )
    name = models.CharField(max_length=20)

    def __str__(self):
        return "{}_{}".format(self.sn, self.name)

    class Meta:
        unique_together = [['sn', 'county']]
        ordering = ['sn']


class Section(models.Model):
    sn = models.CharField(max_length=4)
    area = models.ForeignKey(
        Area,
        on_delete=models.PROTECT,
        related_name="section"
    )
    office = models.CharField(max_length=2)
    name = models.CharField(max_length=20)

    def __str__(self):
        return "{}_{}".format(self.sn, self.name)

    class Meta:
        unique_together = [['sn', 'area']]


class Land(models.Model):
    sn = models.CharField(max_length=8)
    section = models.ForeignKey(
        Section,
        on_delete=models.PROTECT,
        related_name="land",
    )
    cx = models.DecimalField(max_digits=9, decimal_places=6)
    cy = models.DecimalField(max_digits=9, decimal_places=6)
    lx = models.DecimalField(max_digits=9, decimal_places=6)
    ly = models.DecimalField(max_digits=9, decimal_places=6)
    rx = models.DecimalField(max_digits=9, decimal_places=6)
    ry = models.DecimalField(max_digits=9, decimal_places=6)

    def landnum(self):
        if int(self.sn[4:]) == 0:
            return "{}".format(int(self.sn[0:4]))
        else:
            return "{}-{}".format(int(self.sn[0:4]), int(self.sn[4:]))

    def __str__(self):
        return "{}_{}_{}".format(
            self.section.area.name, self.section.name, self.landnum())

    class Meta:
        unique_together = [['sn', 'section']]
