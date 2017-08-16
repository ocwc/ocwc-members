from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from crm.views import IndexView, LoginKeyCheckView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/v1/', include('crm.urls_api', namespace='api', app_name='crm')),
    url(r'^crm/', include('crm.urls', namespace='crm', app_name='crm')),
    url(r'^staff/', include('crm.urls_staff', namespace='staff', app_name='crm')),
    url(r'^application/', include('crm.urls_application', namespace='application')),
    (r'^comments/', include('djangospam.cookie.urls')),

    url(r'^login/(?P<key>[\w|\W]+)/$', LoginKeyCheckView.as_view(), name='login-key-check'),

    url(r'^conferences/', include('conferences.urls', namespace='conferences', app_name='conferences')),
    url(r'^elections/', include('elections.urls', namespace='elections', app_name='elections')),

    url(r'^$', IndexView.as_view(), name='crm_index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^theme/lib/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/gandalf/hacking/mainsite/wp-content/themes/ocwc-mainsite/lib/'}),
        url(r'^theme/images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/gandalf/hacking/mainsite/wp-content/themes/ocwc-mainsite/images/'}),
        url(r'^media/logos/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/gandalf/hacking/members/media/logos/'}),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
