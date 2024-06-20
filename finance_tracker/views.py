from django.shortcuts import render, redirect
from .models import Account, Transaction
from decimal import Decimal
from django.contrib import messages
# Create your views here.

def index_account(request):
    accounts=Account.objects.all()
    return render(request, 'account/index.html', {'accounts': accounts})

def create_account(request):
    return render(request,'account/create.html')

def store_account(request):
    if request.method == 'POST':
        firstName=request.POST.get('first_name')
        lastName=request.POST.get('last_name')
        accountName = request.POST.get('account_name')
        Account.objects.create(account_name=accountName, first_name=firstName, last_name=lastName)
        return redirect('/account')

def delete_account(request, account_id):
    Account.objects.filter(id=account_id).delete() #delete from mysql

    return redirect('/account')


def create_transaction(request, account_id):
    account=Account.objects.get(id=account_id)
    transactions =Transaction.objects.filter(account=account)
    context = {
        'account':account,
        'transaction':transactions
    }
    return render(request, 'transaction/index.html', context)

def save_transaction(request, account_id):
    account = Account.objects.get(id=account_id)
    if request.method == 'POST':
        str_amount=request.POST.get('amount')
        Description=request.POST.get('description')
        transactionType=request.POST.get('transaction_type')
        amount = Decimal(str_amount)
        if transactionType=='withdraw':
            withdraw(request, account,amount, Description)
        elif transactionType=='deposit':
            deposit(account,amount, Description)
        
        return redirect('/account')

    return render(request, 'transaction/index.html', {'account':account}, {'transactions': transactions})

def withdraw(request, account, amount, Description):
    if account.balance >= amount:
        account.balance -= amount
        account.total_expense += amount
        account.save()
        Transaction.objects.create(account=account, amount=amount, description=Description, transaction_type='withdraw')
    else:
        messages.error(request, 'error not a valid transaction')
        return redirect('/account') 

def deposit(account, amount,Description):
        account.balance += amount
        account.total_deposit += amount
        account.save()
        Transaction.objects.create(account=account, amount=amount, description=Description, transaction_type='deposit')

