from django.db import models
from django.core.urlresolvers import reverse




class Store(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    store_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('check:storedetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.store_name


class User(models.Model):
    user_store = models.ForeignKey('Store', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    user_position = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('check:userdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.user_name

class Account(models.Model):
    acount_store = models.ForeignKey('Store', on_delete=models.CASCADE)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)
    account_number = models.CharField(max_length=50)
    routing_number = models.CharField(max_length=50)
    account_name = models.CharField(max_length=50)
    account_street = models.CharField(max_length=50)
    account_state = models.CharField(max_length=50)
    account_city = models.CharField(max_length=50)
    account_zip = models.CharField(max_length=50)
    checks_bounced = models.CharField(max_length=50)
    
    def get_absolute_url(self):
        return reverse('check:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'Account Name: ' + self.account_name + ' - Account Number: ' + self.account_number + ' - Routing Number: ' + self.routing_number

class Check(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    check_amount = models.CharField(max_length=50)
    check_number = models.CharField(max_length=50)
    cashier_name = models.CharField(max_length=50)
    check_status = models.BooleanField(default=False)
    letter_date1 = models.CharField(max_length=50)
    letter_date2 = models.CharField(max_length=50)
    letter_date3 = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('check:checkdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'Check Amount: ' + self.check_amount + ' / Check Number: ' + self.check_number + ' / ' + self.cashier_name

class Client(models.Model):
    client_name = models.CharField(max_length=50)
    def __str__(self):
        return self.client_name


class Bank(models.Model):
    bank_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('check:bankdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.bank_name
