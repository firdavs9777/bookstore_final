from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django admin
    path('anything-admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')), # new

    # Local apps
    path('', include('pages.urls')),
    path('books/',include('books.urls')), #new
    path('orders/',include('orders.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/',include(debug_toolbar.urls)),
    ] + urlpatterns
