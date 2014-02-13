from django.contrib import admin
from projects.models import Project, Link, Language, Catagory
from home.models import Statement

class ProjectAdmin(admin.ModelAdmin):
	filter_horizontal = ('languages', 'links', 'catagories')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Link)
admin.site.register(Language)

admin.site.register(Statement)