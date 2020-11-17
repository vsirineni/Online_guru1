from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'OnlineHobbies'
urlpatterns = [
                  path('', views.online_hobby_list, name='online_hobby_list'),
                  path('online_hobby=_list', views.online_hobby_list, name='online_hobby_list'),
                  # path('online_hobby_list/', login_required(views.online_hobby_list), name='online_hobby_list'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
