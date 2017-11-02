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
    url(r'stores/$', views.StoreIndexView.as_view(), name='storeindex'),
    url(r'clients/$', views.ClientIndexView.as_view(), name='clientindex'),
    url(r'banks/$', views.BankIndexView.as_view(), name='bankindex'),
    url(r'users/$', views.UserIndexView.as_view(), name='userindex'),

    # /check/accounts/account-details/pk/
    url(r'^accounts/account-details/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /check/bank-details/pk/
    url(r'^bank-details/(?P<pk>[0-9]+)/$', views.BankDetailView.as_view(), name='bankdetail'),
    # /check/user-details/pk/
    url(r'^user-details/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='userdetail'),
    # /check/store-details/pk/
    url(r'^store-details/(?P<pk>[0-9]+)/$', views.StoreDetailView.as_view(), name='storedetail'),
    url(r'^client-details/(?P<pk>[0-9]+)/$', views.ClientDetailView.as_view(), name='clientdetail'),

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
    url(r'checks/user-update/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view(), name="user-update"),
    url(r'checks/store-update/(?P<pk>[0-9]+)/$', views.StoreUpdate.as_view(), name="store-update"),
    url(r'checks/bank-update/(?P<pk>[0-9]+)/$', views.BankUpdate.as_view(), name="bank-update"),
    
    # Not Implemented
    # /check/account/pk/delete/
    url(r'^check/check-details/(?P<pk>[0-9]+)/delete/$', views.CheckDelete.as_view(), name="check-delete"),
    url(r'^check/account-details/(?P<pk>[0-9]+)/delete/$', views.AccountDelete.as_view(), name="account-delete"),
    url(r'^check/bank-details/(?P<pk>[0-9]+)/delete/$', views.BankDelete.as_view(), name="bank-delete"),
    url(r'^check/store-details/(?P<pk>[0-9]+)/delete/$', views.StoreDelete.as_view(), name="store-delete"),
    url(r'^check/user-details/(?P<pk>[0-9]+)/delete/$', views.UserDelete.as_view(), name="user-delete"),
    url(r'^check/client-details/(?P<pk>[0-9]+)/delete/$', views.ClientDelete.as_view(), name="client-delete"),
]