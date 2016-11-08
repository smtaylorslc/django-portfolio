from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import landing_page.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', landing_page.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
