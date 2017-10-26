from django.conf.urls import url
from . import views

app_name = 'check'

urlpatterns = [
    # /check/
    url(r'^$', views.index, name='index'),
    # /check/accounts/
    url(r'accounts/$', views.AccountIndexView.as_view(), name='accountindex'),
    # /check/checks/
    url(r'checks/$', views.CheckIndexView.as_view(), name='checkindex'),

    # /check/accounts/account-details/pk/
    url(r'^accounts/account-details/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /check/bank-details/pk/
    url(r'^bank-details/(?P<pk>[0-9]+)/$', views.BankDetailView.as_view(), name='bankdetail'),
    # /check/user-details/pk/
    url(r'^user-details/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='userdetail'),
    # /check/store-details/pk/
    url(r'^store-details/(?P<pk>[0-9]+)/$', views.StoreDetailView.as_view(), name='storedetail'),

    #/check/check-details/pk/
    url(r'^check/check-details/(?P<pk>[0-9]+)/$', views.CheckDetailView.as_view(), name='checkdetail'),

    # /check/account/add/
    url(r'account/add/$', views.AccountCreate.as_view(), name="account-add"),
    # /check/check/add/
    url(r'check/add/$', views.CheckCreate.as_view(), name="check-add"),
    # /check/bank/add/
    url(r'bank/add/$', views.BankCreate.as_view(), name="bank-add"),
    # /check/store/add/
    url(r'store/add/$', views.StoreCreate.as_view(), name="store-add"),
    # /check/user/add/
    url(r'user/add/$', views.UserCreate.as_view(), name="user-add"),
    
    # /check/accounts/acount-update/pk/
    url(r'accounts/account-update/(?P<pk>[0-9]+)/$', views.AccountUpdate.as_view(), name="account-update"),
    # /check/checks/check-update/pk/
    url(r'checks/check-update/(?P<pk>[0-9]+)/$', views.CheckUpdate.as_view(), name="check-update"),
    
    # Not Implemented
    # /check/account/pk/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.AccountDelete.as_view(), name="account-delete"),
]