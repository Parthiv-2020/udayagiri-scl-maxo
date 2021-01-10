from django.contrib import admin
from .models import Teacher
from django.utils.html import format_html

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id', 'name', 'myphoto', 'subject', 'country')
    search_fields = ('name', 'subject')
    # list_filter = ('city', 'camera_type')
    # list_display_links = ('id', 'name')


admin.site.register(Teacher, TeacherAdmin)