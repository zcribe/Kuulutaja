from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls')),
    path('', include('users.urls'))
]

# DEBUG TOOLBAR
if settings.DEBUG:
    import debug_toolbar
    from django.views.defaults import server_error, page_not_found, bad_request, permission_denied
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls))
    ] + urlpatterns

    urlpatterns += [
        path('400/', bad_request, kwargs={'exception': Exception('Bad Request!')}),
        path('403/', permission_denied, kwargs={'exception': Exception('Bad Request!')}),
        path('404/', page_not_found, kwargs={'exception': Exception('Page not Found')}),
        path('500/', server_error),

    ]

