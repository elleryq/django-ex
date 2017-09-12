from django.conf.urls import include, url
from django.contrib import admin

#from welcome.views import index, health
from haodooscraper.views import IndexView

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', IndexView.as_view()),
    # url(r'^health$', health),
    # url(r'^admin/', include(admin.site.urls)),
]
