from django.contrib import admin
from django.urls import path
from .views import group1_view, group2_view, group3_view,base_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base_view, name='base'),
    path('group1/', group1_view, name='group1'),
    path('group2/', group2_view, name='group2'),
    path('group3/', group3_view, name='group3'),
]