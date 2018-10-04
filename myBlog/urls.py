
from django.contrib import admin
from django.urls import path,re_path
from BlogApp import views 
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url






urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('input', views.input),
    path('display', views.display),
    path('save',views.save),
    re_path(r'^writer/(?P<pk>\d+)$', views.writer.as_view()),
    re_path(r'^edite/(?P<pk>\d+)$', views.edite.as_view()),
    re_path(r'^update/(?P<id>\d+)$', views.update),
    re_path(r'^delete/(?P<id>\d+)$', views.delete),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 