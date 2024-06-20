from django.db import models
from decimal import Decimal

# Create your models here.

class Account(models.Model):
    first_name = models.CharField(max_length=55, blank=False)
    last_name =models.CharField(max_length=55, blank=False)
    account_name=models.CharField(max_length=55, blank=False)
    balance=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_expense=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_deposit=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_created=models.DateTimeField(auto_now_add=True)

    
    class Meta:
        db_table = 'accounts'
    
    def __str__(self):
        return self.account_name

class Transaction(models.Model):
    account=models.ForeignKey(Account, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    description=models.CharField(max_length=55)
    transaction_type=models.CharField(max_length=55, choices=[('deposit', 'Deposit'), ('withdraw','Withdraw')])
    date_created = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        db_table = 'transactions'
    
    def __str__(self):
        return self.account.account_name
