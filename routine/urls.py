from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/departments/$', views.departments_list),
    url(r'^api/departments/(?P<pk>[0-9]+)$', views.departments_detail),
]