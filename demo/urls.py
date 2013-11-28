# Copyright (c) 2011,  2012 Free Software Foundation

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.

#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.



"""Urls for the demo of Gstudio"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.defaults import url
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import password_change,password_change_done,login, password_reset_confirm, password_reset, password_reset_done	
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.decorators import login_required

from gstudio.sitemaps import TagSitemap
from gstudio.sitemaps import NodetypeSitemap
from gstudio.sitemaps import MetatypeSitemap
from gstudio.sitemaps import AuthorSitemap
from gstudio.forms import *
from objectapp.sitemaps import GbobjectSitemap

from registration.views import register
from views import home_view, more_view,proceed_view
from decorator import decorated_includes


admin.autodiscover()
handler500 = 'demo.views.server_error'
handler404 = 'django.views.defaults.page_not_found'

urlpatterns = patterns(
    '',
    (r'^$', 'django.views.generic.simple.redirect_to',
     {'url': '/home/'}),
    url(r'^home/', home_view),
    url(r'^proceed', proceed_view),
    url(r'^browserError/', direct_to_template, {'template': 'gstudio/browserError.html'}),
   # url(r'^more/',more_view),
    #urls for ison static html pages
    url(r'^ison/about/', direct_to_template, {'template': 'ison-html/about.html'}),
   url(r'^ison/resources/', direct_to_template, {'template': 'ison-html/resource_type.html'}),
    url(r'^ison/posters/', direct_to_template, {'template': 'ison-html/resources_posters.html'}),
    url(r'^ison/posters-gallery/', direct_to_template, {'template': 'ison-html/poster_gallery.html'}),
    url(r'^ison/handbook/', direct_to_template, {'template': 'ison-html/resources_handbooks.html'}),
   url(r'^ison/ppts/', direct_to_template, {'template': 'ison-html/resources_ppts.html'}),
   url(r'^ison/videos/', direct_to_template, {'template': 'ison-html/resources_videos.html'}),
   url(r'^ison/workshops-list/', direct_to_template, {'template': 'ison-html/workshops.html'}),
  url(r'^ison/workshops-state/', direct_to_template, {'template': 'ison-html/workshop_list_state.html'}),
  url(r'^ison/workshops-date/', direct_to_template, {'template': 'ison-html/workshop_list_date.html'}),
  url(r'^ison/workshops-look/', direct_to_template, {'template': 'ison-html/workshops_look.html'}),
   url(r'^ison/bangalore/', direct_to_template, {'template': 'ison-html/bangalore.html'}),
   url(r'^ison/bhopal/', direct_to_template, {'template': 'ison-html/bhopal.html'}),
   url(r'^ison/guwahati/', direct_to_template, {'template': 'ison-html/guwahati.html'}),
   url(r'^ison/workshop-resources/', direct_to_template, {'template': 'ison-html/workshop_resources.html'}),
   url(r'^ison/vainu-bappu/', direct_to_template, {'template': 'ison-html/vainubappu.html'}),
   url(r'^ison/how-to-see-ison/', direct_to_template, {'template': 'ison-html/ephemeris.html'}),
   url(r'^ison/useful-links/', direct_to_template, {'template': 'ison-html/useful_links.html'}),
 url(r'^ison/karnataka/', direct_to_template, {'template': 'ison-html/karnataka.html'}),
 url(r'^ison/media/', direct_to_template, {'template': 'ison-html/inthemedia.html'}),
 url(r'^ison/ison-india/', direct_to_template, {'template': 'ison-html/ison-india.html'}),
 url(r'^ison/contact/', direct_to_template, {'template': 'ison-html/contact.html'}),
 url(r'^ison/faqs/', direct_to_template, {'template': 'ison-html/faqs.html'}),
 url(r'^ison/latest/', direct_to_template, {'template': 'ison-html/latestnews.html'}),


    url(r'^ison/', include('gstudio.urls')),
    url(r'^gstudio/', include('gstudio.urls')),
    url(r'^nodetypes/', include('gstudio.urls')),
    url(r'^objects/', include('objectapp.urls')),
    #url(r'^tagclouds/',include('gstudio.urls.tagclouds')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^browsecollection/','gstudio.views.browseCollection.browseCollection'),
    url(r'^collection/(\w+)/','gstudio.views.collection.collection'),
    url(r'^AboutUs/', direct_to_template, {'template': 'gstudio/aboutUs.html'}),
    url(r'^TermsOfUse/', direct_to_template, {'template': 'gstudio/termsOfUse.html'}),
    url(r'^ContactUs/', direct_to_template, {'template': 'gstudio/contactUs.html'}),
    url(r'^Contribute/', direct_to_template, {'template': 'gstudio/contribute.html'}),
    #URL for XMLRPC
    #url(r'^xmlrpc/$','django_xmlrpc.views.handle_xmlrpc'),
    #url(r'^i18n/', include('django.conf.urls.i18n')),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/gstudio/', include('gstudio.urls.ajaxurls')),
    url(r'^admin/password_change/', password_change,{'password_change_form':UserChangeform,'template_name':'registration/password_change_form1.html'}),
    url(r'^account/password/change/', password_change,{'password_change_form':UserChangeform,'template_name':'registration/password_change_form1.html'}),
    url(r'^accounts/password/change/done/', password_change_done,{'template_name':'registration/password_change_done1.html'}),
    url(r'^admin/', decorated_includes(login_required,include(admin.site.urls))),
    url(r'^objects/admin/', decorated_includes(login_required,include(admin.site.urls))),
    url(r'^nodetypes/admin/', decorated_includes(login_required,include(admin.site.urls))),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^notification/',include('notification.urls')),
    url(r'^accounts/register/$', register, {'backend': 'gstudio.regbackend.MyBackend','form_class': UserRegistrationForm}, name='registration_register'),
    url(r'^accounts/login/', login,{'authentication_form':UserLogin}),
    url(r'^accounts/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm,{'set_password_form':UserResetform,'template_name':'registration/password_reset_confirm1.html'}),
    url(r'^accounts/password/reset/done/', password_reset_done,{'template_name':'registration/password_reset_done1.html'}),
    url(r'^accounts/password/reset/', password_reset,{'template_name':'registration/password_reset_form1.html'}),
    url(r'^accounts/', include('registration.urls')),

    url(r'^$', 'django.views.generic.simple.redirect_to',
            { 'template': 'index.html' }, 'index'),
    )

sitemaps = {'tags': TagSitemap,
            'blog': NodetypeSitemap,
            'authors': AuthorSitemap,
            'objecttypes': MetatypeSitemap,
            'gbobjects': NodetypeSitemap}

urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
        {'sitemaps': sitemaps}),
    )

urlpatterns += patterns(
    '',
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^500/$', 'demo.views.server_error'),
    )

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT})
        )
