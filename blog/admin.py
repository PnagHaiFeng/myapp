from django.contrib import admin
from .models import  Blog,BlogType

@admin.register(BlogType)
class blogType(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class blog(admin.ModelAdmin):
    list_display = ('id','title', 'content','created_time','author',  'last_updated_time','blog_type')
    list_filter = ['title']  # 过虑器
    search_fields = ['title']  # 查找栏的意思
    list_per_page = 5
    actions_on_top = False
    actions_on_bottom = True


