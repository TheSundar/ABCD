from __future__ import unicode_literals

from django.db import models

# Create your models here.
class HomeWork(models.Model):
    school_name = models.CharField(max_length=50)
    student_name = models.CharField(max_length=25)
    student_class = models.CharField(max_length=10)
    student_hw_sub1 = models.CharField(max_length=1000)
    student_hw_sub2 = models.CharField(max_length=1000)
    student_hw_sub3 = models.CharField(max_length=1000)
    student_hw_sub4 = models.CharField(max_length=1000)
    student_hw_sub5 = models.CharField(max_length=1000)
    student_hw_sub6 = models.CharField(max_length=1000)
    
    
    def __str__(self):
        return self.student_name