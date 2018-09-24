from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')), # include all .urls of all apps created here so that it can be accessed
    path('store/', include('store.urls')),
]
