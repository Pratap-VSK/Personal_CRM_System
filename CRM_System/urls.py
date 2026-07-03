from django.contrib import admin
from django.urls import include, path

from crm.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('', include('crm.urls')),
]
