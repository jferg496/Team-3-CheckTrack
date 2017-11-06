from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^check/', include('check.urls')),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view()),
    url('^', include('django.contrib.auth.urls')),
]



