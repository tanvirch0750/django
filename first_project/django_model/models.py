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
        
        
# One to to one relationship
class Person(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Passport(models.Model):
    user = models.OneToOneField(to=Person, on_delete=models.CASCADE)
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()
    
# One to many / many to one relationship
class Post(models.Model):
    user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    post_cap = models.CharField(max_length=50)
    post_details = models.CharField(max_length=100)
    
    
# many to many relation
class Student2(models.Model):
    name = models.CharField(max_length=30)
    class_name = models.CharField(max_length=10)
    roll = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    student = models.ManyToManyField(Student2)
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    
    def student_list(self):
        return ",".join([str(i) for i in self.student.all()])
    
    
    
    

    
    

