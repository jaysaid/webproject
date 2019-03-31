from django.contrib import admin
from hzapp import models
# Register your models here.


# class UserProfileAdmin(admin.ModelAdmin):
    # list_display = ('user', 'name', 'get_email', 'get_is_active')  # 定义admin总览里每行的显示信息，由于email是在userprofile的外键user表中，所以需要特殊返回，注意这个字段不能用user__email的形式
    # search_fields = ('user__username', 'name')  # 定义搜索框以哪些字段可以搜索，因为username是在user表中，所以用user__username的形式，这里需要注意下，不能直接用user表名，要用字段名，表名__字段名
    # list_filter = ('user__groups', 'user__is_active')  #传入的需要是列表，设定过滤列表

    # def get_email(self, obj):  # 定义这个函数是由于email是在userprofile表的外键表user里，所以需要单独return一下
        # return obj.user.email
    # get_email.short_description = 'Email'  #list展示时候显示的title
    # get_email.admin_order_field = 'user__email'  #指定排序字段

    # def get_is_active(self, obj):
        # return obj.user.is_active
    # get_is_active.short_description = '有效'
    # get_is_active.admin_order_field = 'user__is_active'


# admin.site.register(models.UserProfile, UserProfileAdmin)