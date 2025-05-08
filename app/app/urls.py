from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # Import static function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the API URLs
    path('api/exam/', include('api.exam_urls')),
    path('api/', include('api.product_urls')),  # This mounts /api/product/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
