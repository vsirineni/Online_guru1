from django.contrib import admin
from .models import OnlineClass, OnlineClassVideoPage, OnlineClassEnroll
admin.site.register(OnlineClass)
admin.site.register(OnlineClassVideoPage)
admin.site.register(OnlineClassEnroll)

# Please clean up below if not needed - Apr 9 2020
#
# class OnlineHobbies(admin.ModelAdmin):
#     list_display = ('online_hobby_name', 'description', 'get_started')
#     list_filter = ( 'online_hobby_name')
#     search_fields = ('online_hobby_name', )
#     ordering = ['online_hobby_name']
#
#
# # class OnlineList(admin.ModelAdmin):
# #     list_display = ('online_hobby_name', 'description', 'get_started')
# #     # list_filter = ( 'cust_name', 'organization')
# #     # search_fields = ('cust_name', )
# #     # ordering = ['cust_name']




