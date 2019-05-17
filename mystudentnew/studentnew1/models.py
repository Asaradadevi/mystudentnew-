from django.db import models

# Create your models here.
class Student(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Register_number = models.PositiveIntegerField(default=0)
    Enrolled_year = models.PositiveIntegerField(default=0)
    Course = models.CharField(max_length=2)
    Branch = models.CharField(max_length=3)

    def __str__(self):
        return self.First_name

class Subject(models.Model):
    Subject_code = models.CharField(max_length=8)
    Subject_title = models.CharField(max_length=50)
    Faculty_name = models.CharField(max_length=30)
    Semester = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.Subject_title

class Mark(models.Model):
    #student = models.ForeignKey(Student, on_delete = models.CASCADE)
    First_name = models.CharField(max_length=30)
    Register_number = models.PositiveIntegerField(default=0)
    Subject_title = models.CharField(max_length=50)
    #subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    cat1_mark = models.PositiveIntegerField(default=0)
    cat2_mark = models.PositiveIntegerField(default=0)
    cat3_mark = models.PositiveIntegerField(default=0)

    def __str__(self):
        return  self.First_name +"-"+ str(self.cat1_mark) + ", " + str(self.cat2_mark)+ ", " + str(self.cat3_mark) +"  in  "+ self.Subject_title
