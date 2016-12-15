"""my_anki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from posts import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page ),
    url(r'^login/$', views.login1 ),
    url(r'^register/$', views.register1),
    url(r'^cards/$', views.user_loged, name='cards'), 
    url(r'^cards/(?P<username>[\w.@+-]+)/(?P<cardname>[\w.@+-]+)/(?P<order>\d+)/(?P<odp>[\w.@+-]+)/$', views.test_catch),
    url(r'^addquestion/$', views.add_question),
    url(r'^cards/delete/(?P<username>[\w.@+-]+)/(?P<cardname>[\w.@+-]+)/$', views.delete_card),
    url(r'^cards/edit/(?P<username>[\w.@+-]+)/(?P<cardname>[\w.@+-]+)/$', views.edit_cards),
    url(r'^cards/edit/(?P<username>[\w.@+-]+)/(?P<cardname>[\w.@+-]+)/(?P<order>\d+)/$', views.del_single_card),
    url(r'^cards/editcard/(?P<username>[\w.@+-]+)/(?P<cardname>[\w.@+-]+)/(?P<order>\d+)/$', views.edit_single_card),
    url(r'^regsuccess/$', views.register_sussess, name = 'success'), 
    url(r'^logout/$', views.logout1), 


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
