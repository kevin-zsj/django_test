from django.conf.urls import patterns, include, url
from django.contrib import admin

# urlpatterns = [
#     # Examples:
#     url(r'^$', 'lists.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     # url(r'^admin/', include(admin.site.urls)),
# ]
urlpatterns = patterns('',
url(r'^$', 'lists.views.home_page', name='home'),
)