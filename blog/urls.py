from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
  path('admin/', admin.site.urls),
  # path('', include('blog.urls')),
  path('', views.post_list, name='post_list'),
]

