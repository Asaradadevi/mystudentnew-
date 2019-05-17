from django.contrib import admin

# Register your models here.

from .models import Student,Subject,Mark

class StudentAdmin(admin.ModelAdmin):
    list_display = ['First_name','Last_name','Register_number','Enrolled_year','Course','Branch']
admin.site.register(Student, StudentAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['Subject_code','Subject_title','Faculty_name','Semester']
admin.site.register(Subject, SubjectAdmin)

class MarkAdmin(admin.ModelAdmin):
    list_display = ['Register_number','Subject_title','cat1_mark','cat2_mark','cat3_mark']
admin.site.register(Mark, MarkAdmin)
