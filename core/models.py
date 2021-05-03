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






