"""wanderlust URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from signup import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$',views.login, name='login'),
	url(r'^description/$',views.description, name='description'),
	url(r'^$', views.home, name='home'),
	#url(r'^state/(?P<pk>[a-zA-Z0-9 ]+)/(?P<p>[a-zA-Z0-9 ]+)/$',views.state,name = 'state'),
	url(r'^state/$',views.state,name = 'state'),
	url(r'^reviews/$', views.review, name='reviews'),
	url(r'^writereview/$' ,views.writereview, name='writereview'),
	url(r'^search/$', views.search, name='search'),
	url(r'^account/$',views.account, name='account'),
	url(r'^administrator/$', views.admin, name='admin'),
	url(r'^databases/$',views.databases, name = 'databases'),
	url(r'^userchange/$',views.userchange, name = 'userchange'),
	url(r'^statechange/$',views.statechange, name = 'statechange'),
	url(r'^historychange/$',views.historychange, name = 'historychange'),
	url(r'^reviewchange/$',views.reviewchange, name = 'reviewchange'),
	url(r'^destinationchange/$',views.destinationchange, name = 'destinationchange'),
	url(r'^passwordchange/$',views.passwordchange, name='passwordchange'),
	url(r'^homesecond/$', views.homesecond, name='homesecond'),
	url(r'^recentsearch/$', views.recent_search, name='recentsearch'),
	url(r'^delete/$',views.delete, name='delete'),
	
]
