from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webpage.urls')),
    path('sales/', include('sales.urls')),
]