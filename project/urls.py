"""cars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'main.views.home'),
    url(r'^car_list_view/$', 'main.views.car_list_view'),
    url(r'^car_search/(?P<car>\w+)/$', 'main.views.car_search'),
    url(r'get_car_search/$', 'main.views.get_car_search'),
    url(r'^car_list_template/$', 'main.views.car_list_template'),
    url(r'^form_view/$', 'main.views.form_view'),
    url(r'^car_detail/(?P<pk>\w+)/$', 'main.views.car_detail'),
    url(r'^signup/$', 'main.views.signup'),
    url(r'^login_view/$', 'main.views.login_view'),
    url(r'^logout_view/$', 'main.views.logout_view'),
    url(r'^add_review/$', 'main.views.add_review'),
    url(r'^car_create/$', 'main.views.car_create'),
    url(r'^origin_list_template/(?P<origin>\w+)/$', 'main.views.origin_list_template'),
    url(r'^about/', 'main.views.about'),
    url(r'^contact/', 'main.views.contact')





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

