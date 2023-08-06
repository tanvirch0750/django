from django.contrib import admin

from . import models

# Register your models here.
# admin.site.register(models.Student)
# admin.site.register(models.StudentInfoModel)
# admin.site.register(models.TeacherInfoModel)
# admin.site.register(models.EmployeeModel)
# admin.site.register(models.ManagerModel)


# @admin.register(models.EmployeeModel)
# class EmployeeModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'city', 'designation')
    
    
# @admin.register(models.ManagerModel)
# class ManagerModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'city', 'designation', 'take_interview', 'hiring') 

# @admin.register(models.Friend)
# class FriendModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'school', 'section', 'attendence', 'class_teacher', 'hw')
    
    
# @admin.register(models.Me)
# class MeModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'school', 'section', 'attendence', 'class_teacher', 'hw')

# @admin.register(models.Person)
# class PersonModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'city', 'email')
    
    
# @admin.register(models.Passport)
# class PassportModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'pass_number', 'page', 'validity')

# @admin.register(models.Post)
# class PostModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'post_cap', 'post_details')

@admin.register(models.Student2)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'class_name')
    
    
@admin.register(models.Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'student_list', 'mobile')
