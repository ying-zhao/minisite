from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^getUserList/', 'restapi.views.getUserList'),
    url(r'^login/', 'restapi.views.login'),
    url(r'^modifyEmail/', 'restapi.views.modifyEmail'),

)