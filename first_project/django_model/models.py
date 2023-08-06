from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField(primary_key=True)
    father_name = models.CharField(max_length=30)
    address = models.TextField()
    
    def __str__(self) -> str:
        return f"Rolle: {self.roll} - {self.name}"
    
    
    
# Modle inheritance and abstract class
class CommonInfoClass(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    
    class Meta:
        abstract = True


class StudentInfoModel(CommonInfoClass):
    roll = models.IntegerField()
    payment = models.IntegerField()
    section = models.CharField(max_length=15)

class TeacherInfoModel(CommonInfoClass):
    salary = models.IntegerField()
    
    
# Multilevel inheritance
class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    
class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()
    
    
# Proxy model
class Friend(models.Model): # my friend is present in class
    school = models.CharField(max_length=40)
    section = models.CharField(max_length=10)
    class_teacher = models.CharField(max_length=20)
    attendence = models.BooleanField()
    hw = models.CharField(max_length=50)
    
    
class Me(Friend): # I am not present in class
    class Meta:
        proxy = True
        ordering = ['id']
    
    
    
    

    
    

