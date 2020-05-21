from django.contrib import admin
from college.models import Notice
# Register your models here.
from django.contrib.admin import ModelAdmin

from college.models import Branch

from college.models import Profile


class NoticeAdmin(ModelAdmin):
    list_display = ["subject", "cr_date"]
    search_fields = ["subject", "cr_date"]
    list_filter = ["cr_date"]
admin.site.register(Notice,NoticeAdmin)
admin.site.register(Branch)
admin.site.register(Profile)
