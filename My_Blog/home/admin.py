from django.contrib import admin
#
# Register your models here.
from .models import Experience, Personal_Detail, Interest, Project, Project_Blog, Project_Blog_Post, Personal_Blog, Image, File
#
# admin.site.register(Post)
admin.site.register(Personal_Detail)
admin.site.register(Experience)
admin.site.register(Interest)
admin.site.register(Project)
admin.site.register(Project_Blog)
admin.site.register(Project_Blog_Post)
admin.site.register(Personal_Blog)
admin.site.register(Image)
admin.site.register(File)




