from django.contrib import admin
from django.contrib.auth.models import User

from .models import BascicSettings, Cate,BlogInfo

from .models import Profile
from django.utils.html import format_html
# Register your models here.
class AdminCat(admin.ModelAdmin):
    def image_tag(self,obj):
        return format_html('<img src="{}" width = 100px/>'.format(obj.c_img.url))
    image_tag.short_description = "Image"
    list_display =['c_name','c_img','c_status','image_tag']
    list_editable=['c_status']

admin.site.register(Cate,AdminCat)
admin.site.register(BlogInfo)
admin.site.register(Profile)
admin.site.register(BascicSettings)