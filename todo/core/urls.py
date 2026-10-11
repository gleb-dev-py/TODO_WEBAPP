from django.contrib import admin
from django.urls import path
from page_one import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.html_render, name='todo'),
    path('tasks', views.save_task, name='save_task')
]
