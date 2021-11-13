from django.contrib import admin
from .models import StudentDashboard,StudentDetail
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('sr_no','name','birthdate')

class StudentDataAdmin(admin.ModelAdmin):
    list_display = ('name','email','mob_no','DOB','profile_img')

admin.site.register(StudentDetail,StudentDataAdmin)
admin.site.register(StudentDashboard,StudentAdmin)
