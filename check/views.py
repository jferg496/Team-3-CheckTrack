from django.views import generic
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Account, Check, Bank, Store, User

def index(request):
    all_accounts = Account.objects.all()
    template = loader.get_template('check/index.html')
    context = {'all_accounts': all_accounts,}
    return HttpResponse(template.render(context, request))

class AccountIndexView(generic.ListView):
    template_name = 'check/accounts.html'
    context_object_name = 'all_accounts'

    def get_queryset(self):
        return Account.objects.all()

class CheckIndexView(generic.ListView):
    template_name = 'check/checks.html'
    context_object_name = 'all_checks'

    def get_queryset(self):
        return Check.objects.all()

class DetailView(generic.DetailView):
    model = Account
    template_name = 'check/detail.html'

class BankDetailView(generic.DetailView):
    model = Bank
    template_name = 'check/bankdetail.html'

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'check/userdetail.html'

class StoreDetailView(generic.DetailView):
    model = Store
    template_name = 'check/storedetail.html'

class CheckDetailView(generic.DetailView):
    model = Check
    template_name = 'check/checkdetail.html'

class AccountCreate(CreateView):
    model = Account
    fields = ['bank', 'acount_store', 'account_number', 'routing_number', 'account_name', 'account_street', 'account_state', 'account_city', 'account_zip', 'checks_bounced']

class CheckCreate(CreateView):
    model = Check
    fields = ['user', 'account', 'check_amount', 'check_number', 'cashier_name', 'letter_date1', 'letter_date2', 'letter_date3', 'check_status']


class BankCreate(CreateView):
    model = Bank
    fields = ['bank_name']

class StoreCreate(CreateView):
    model = Store
    fields = ['client', 'store_name']

class UserCreate(CreateView):
    model = User
    fields = ['user_store', 'user_name', 'user_position']

class AccountUpdate(UpdateView):
    model = Account
    fields = ['account_number', 'routing_number', 'account_name', 'account_street', 'account_state', 'account_city', 'account_zip', 'checks_bounced']

class CheckUpdate(UpdateView):
    model = Check
    fields = ['user', 'account', 'check_amount', 'check_number', 'cashier_name', 'letter_date1', 'letter_date2', 'letter_date3', 'check_status']


class AccountDelete(DeleteView):
    model = Account
    success_url = reverse_lazy('check:index')