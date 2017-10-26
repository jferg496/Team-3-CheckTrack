from django.conf.urls import url
from . import views

app_name = 'check'

urlpatterns = [
    # /check/
    url(r'^$', views.index, name='index'),

    url(r'accounts/$', views.AccountIndexView.as_view(), name='accountindex'),

    # /check/checks/
    url(r'checks/$', views.CheckIndexView.as_view(), name='checkindex'),

    #/account/pk/
    url(r'^accounts/account-details/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^bank-details/(?P<pk>[0-9]+)/$', views.BankDetailView.as_view(), name='bankdetail'),

    url(r'^user-details/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='userdetail'),

    url(r'^store-details/(?P<pk>[0-9]+)/$', views.StoreDetailView.as_view(), name='storedetail'),

    #/check/pk/
    url(r'^check/check-details/(?P<pk>[0-9]+)/$', views.CheckDetailView.as_view(), name='checkdetail'),

    # /check/account/add/
    url(r'account/add/$', views.AccountCreate.as_view(), name="account-add"),

    url(r'check/add/$', views.CheckCreate.as_view(), name="check-add"),

    url(r'bank/add/$', views.BankCreate.as_view(), name="bank-add"),

    url(r'store/add/$', views.StoreCreate.as_view(), name="store-add"),

    url(r'user/add/$', views.UserCreate.as_view(), name="user-add"),
    
    # /check/account/pk/
    url(r'accounts/account-update/(?P<pk>[0-9]+)/$', views.AccountUpdate.as_view(), name="account-update"),
    
    # /check/account/pk/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.AccountDelete.as_view(), name="account-delete"),
]