from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('running_text', views.video_request_view, name='running_text'),
]