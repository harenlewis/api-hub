from django.contrib import admin

from .models import Project, Api, APIPermissions


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'uuid', 'created_by', 'created_at',
                    'modified_by', 'modified_at')
    search_fields = ('name', )
    list_filter = ('created_at',)


class ApiAdmin(admin.ModelAdmin):
    list_display = ('project', 'path', 'method', 'res_type', 'res_body',
                    'created_by', 'created_at', 'modified_by', 'modified_at')
    search_fields = ('project__name', 'res_body')
    list_filter = ('created_at', 'method', 'res_type')


class APIPermissionsAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'permission', 'created_by',
                    'created_at', 'modified_by', 'modified_at')
    search_fields = ('project__name', 'user__username')
    list_filter = ('created_at', 'permission')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Api, ApiAdmin)
admin.site.register(APIPermissions, APIPermissionsAdmin)