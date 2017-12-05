from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Account, Check, Bank, Store, Client
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.utils import timezone

def logout(request):
    logout(request)

@login_required(login_url="/login/")
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

class ReportIndexView(generic.ListView):
    template_name = 'check/report.html'
    context_object_name = 'all_checks'

    def get_queryset(self):
        return Check.objects.all()

class StoreIndexView(generic.ListView):
    template_name = 'check/store.html'
    context_object_name = 'all_stores'

    def get_queryset(self):
        return Store.objects.all()

class ClientIndexView(generic.ListView):
    template_name = 'check/client.html'
    context_object_name = 'all_clients'

    def get_queryset(self):
        return Client.objects.all()

class BankIndexView(generic.ListView):
    template_name = 'check/bank.html'
    context_object_name = 'all_banks'

    def get_queryset(self):
        return Bank.objects.all()

class DetailView(generic.DetailView):
    model = Account
    template_name = 'check/detail.html'

class BankDetailView(generic.DetailView):
    model = Bank
    template_name = 'check/bankdetail.html'



class StoreDetailView(generic.DetailView):
    model = Store
    template_name = 'check/storedetail.html'

class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'check/clientdetail.html'

class CheckDetailView(generic.DetailView):
    model = Check
    template_name = 'check/checkdetail.html'

class LetterOneDetailView(generic.DetailView):
    model = Check
    template_name = 'check/letterone.html'

    def get_queryset(self):
        return Check.objects.all()

class LetterTwoDetailView(generic.DetailView):
    model = Check
    template_name = 'check/lettertwo.html'

    def get_queryset(self):
        return Check.objects.all()

class LetterThreeDetailView(generic.DetailView):
    model = Check
    template_name = 'check/letterthree.html'

    def get_queryset(self):
        return Check.objects.all()
        
    
class AccountCreate(CreateView):
    model = Account
    fields = ['bank', 'acount_store', 'account_number', 'routing_number', 'account_name', 'account_street', 'account_state', 'account_city', 'account_zip', 'checks_bounced']

class CheckCreate(CreateView):
    model = Check
    fields = ['account', 'check_amount', 'check_number', 'cashier_name', 'check_status']


class BankCreate(CreateView):
    model = Bank
    fields = ['bank_name']

class StoreCreate(CreateView):
    model = Store
    fields = ['client', 'store_name']



class AccountUpdate(UpdateView):
    model = Account
    fields = ['account_number', 'routing_number', 'account_name', 'account_street', 'account_state', 'account_city', 'account_zip', 'checks_bounced']

class CheckUpdate(UpdateView):
    model = Check
    fields = ['account', 'check_amount', 'check_number', 'cashier_name', 'check_status']

class LetterOne(UpdateView):
    model = Check
    fields = ['letter_date_1']
    def get_initial(self):
        return { 'letter_date_1': datetime.now() }

class LetterTwo(UpdateView):
    model = Check
    fields = [ 'letter_date_2']
    def get_initial(self):
        return { 'letter_date_2': datetime.now() }
class LetterThree(UpdateView):
    model = Check
    fields = ['letter_date_3']
    def get_initial(self):
        return { 'letter_date_3': datetime.now() }

class BankUpdate(UpdateView):
    model = Bank
    fields = ['bank_name']

class StoreUpdate(UpdateView):
    model = Store
    fields = ['client', 'store_name']



class CheckDelete(DeleteView):
    model = Check
    success_url = reverse_lazy('check:checkindex')

class AccountDelete(DeleteView):
    model = Account
    success_url = reverse_lazy('check:accountindex')

class BankDelete(DeleteView):
    model = Bank
    success_url = reverse_lazy('check:index')

class StoreDelete(DeleteView):
    model = Store
    success_url = reverse_lazy('check:index')


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('check:index')
