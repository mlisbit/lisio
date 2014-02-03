from django.contrib import admin
from projects_app.models import Project, Link, Language
from models import Statement

class ProjectAdmin(admin.ModelAdmin):
	filter_horizontal = ('languages', 'links')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Link)
admin.site.register(Language)

admin.site.register(Statement)