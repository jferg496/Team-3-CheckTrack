from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta
from django.utils import timezone

class Store(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    store_name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('check:storedetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.store_name


class Account(models.Model):
    acount_store = models.ForeignKey('Store', on_delete=models.CASCADE)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)
    account_number = models.IntegerField(max_length=10)
    account_name = models.CharField(max_length=20)
    account_street = models.CharField(max_length=50)
    account_state = models.CharField(max_length=20)
    account_city = models.CharField(max_length=20)
    account_zip = models.CharField(max_length=10)
    checks_bounced = models.IntegerField(max_length=1)
    
    def get_absolute_url(self):
        return reverse('check:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.account_name + ' - Account Number: ' + str(self.account_number)

class Check(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    check_amount = models.IntegerField(max_length=10)
    check_number = models.IntegerField(max_length=4)
    cashier_name = models.CharField(max_length=20)
    check_status = models.BooleanField(default=False)
    entry_date = models.DateTimeField(auto_now_add=True, blank=True)
    letter_date_1 = models.DateField(null=True, blank=True)
    letter_date_2 = models.DateField(null=True, blank=True)
    letter_date_3 = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('check:checkdetail', kwargs={'pk': self.pk})
    
    def two_weeks(self):
        if self.letter_date_1 is None and self.check_status is False:
            return True
    def four_weeks(self):
        if self.letter_date_1 is not None and self.letter_date_2 is None and self.check_status is False and self.entry_date < (timezone.now() - timedelta(days=14)):
            return True
    def six_weeks(self):
        if self.letter_date_1 is not None and self.letter_date_2 is not None and self.letter_date_3 is None and self.check_status is False and self.entry_date < (timezone.now() - timedelta(days=28)):
            return True
        
    def __str__(self):
        return 'Check Amount: ' + str(self.check_amount) + ' / Check Number: ' + str(self.check_number) + ' / ' + self.cashier_name

class Client(models.Model):
    client_name = models.CharField(max_length=50)
    def __str__(self):
        return self.client_name


class Bank(models.Model):
    bank_name = models.CharField(max_length=50)
    routing_number = models.IntegerField(default=1, max_length=9)
    def get_absolute_url(self):
        return reverse('check:bankdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.bank_name + ' - ' + str(self.routing_number)
