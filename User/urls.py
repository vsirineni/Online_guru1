from django.urls import path, include
from django.conf.urls import url
from .views import PasswordResetMPSEmailView, SignUpView, edit_profile, contact
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView,\
    PasswordResetDoneView, PasswordResetConfirmView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('change-password/', PasswordChangeView.as_view(), name='password_change'),
    path('change-password-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset-form/', PasswordResetMPSEmailView.as_view(), name='password_reset_form'),
    path('password-reset-done-form/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('review/', views.contact, name='review'),
    path('review_thankyou/', TemplateView.as_view(template_name='review_thankyou.html'), name='review_thankyou'),
    path('classes/', login_required(TemplateView.as_view( template_name='classes.html')), name='classes'),
    path('profile_preview/', TemplateView.as_view(template_name='profile_preview.html'), name='profile_preview'),
    path('profile/', views.edit_profile, name='profile'),
    path('hobby_list/', login_required(views.hobby_list), name='hobby_list'),
    path('online_hobby_list/', login_required(views.online_hobby_list), name='online_hobby_list'),
    path('online_hobby_video_page/<int:pk>/', login_required(views.online_onclick_getstarted), name='online_class_video_page'),
    path('online_hobby_enroll/<int:pk>/', login_required(views.online_class_enroll), name='online_class_enroll'),
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', views.add_to_cart, name="add_to_cart"),
    url(r'^order-summary/$', views.order_details, name="order_summary"),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', views.delete_from_cart, name='delete_item'),
    url(r'^order_confirm/$', views.order_confirm, name="order_checkout"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

