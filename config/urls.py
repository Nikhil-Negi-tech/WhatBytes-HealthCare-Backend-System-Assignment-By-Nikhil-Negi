from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    # API endpoints
    path('api/auth/', include('accounts.urls')),
    # Core app endpoints
    path('api/', include('core.urls')),
]
