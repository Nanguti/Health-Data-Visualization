from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('data.urls')),
    path('api/v1/locations/', include('locations.urls'))
]
