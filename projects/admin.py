from django.contrib import admin
from projects.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'technology', 'image', 'link')

admin.site.register(Project, ProjectAdmin)
