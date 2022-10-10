from Django.contrib import admin
from Django.urls import path, include
from Django.conf import settings
from Django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('api-auth', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)