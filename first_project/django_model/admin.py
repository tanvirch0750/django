from django.contrib import admin

from . import models

# Register your models here.
# admin.site.register(models.Student)
# admin.site.register(models.StudentInfoModel)
# admin.site.register(models.TeacherInfoModel)
# admin.site.register(models.EmployeeModel)
# admin.site.register(models.ManagerModel)


@admin.register(models.EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'designation')
    
    
@admin.register(models.ManagerModel)
class ManagerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'designation', 'take_interview', 'hiring')
    
    

