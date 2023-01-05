from django.contrib import admin

from app.models import *
admin.site.site_header = '乳腺癌诊断系统' #  登录显示
admin.site.site_title = '乳腺癌登录系统后台' # title
admin.site.index_title = '乳腺癌后台管理' #

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list_display用于设置列表页面要显示的不同字段
    list_display = ['id','name','tel','password']
    # search_fields用于设置搜索栏中要搜索的不同字段
    search_fields = ['id','name','tel','password']

