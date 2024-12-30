from django.contrib import admin
from django.urls import path, include
from django.conf import settings # importing settings module
from django.conf.urls.static import static
import tweets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweets/', include('tweets.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
