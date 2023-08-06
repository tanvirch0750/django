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
    
    

    
    

