from django.shortcuts import render
from django.contrib import messages
from .forms import RegisterNewTransactionFrom
from django.core.paginator import Paginator

from tracker.views import check_if_user_loggedin
from .models import Transactions
from .filters import TransactionFilter

# Create your views here.


def user_home_page(request):
    user = check_if_user_loggedin(request)
    user_transactions = Transactions.objects.filter(user=user)
    context = {'form': RegisterNewTransactionFrom(),
               'transactions': user_transactions.order_by('-id')[:10]}
    return render(request, "index.html", context)


def monthly_report(request):
    return render(request, "monthly-report.html", {})


def history(request):
    user = check_if_user_loggedin(request)
    transactions = Transactions.objects.filter(
        user=user)
    transactions_filtered = TransactionFilter(
        request.GET, queryset=transactions)
    # paginator = Paginator(Transactions.objects.filter(
    #     user=user).order_by('-id'), 15)
    # page_number = request.GET.get('page')
    # page_obj = Paginator.get_page(paginator, page_number)
    # context = {'transactions': page_obj}
    context = {'form': transactions_filtered.form,
               'transactions': transactions_filtered.qs.order_by('-id')}

    return render(request, "history.html", context)


def add_expense(request):
    if request.method == 'POST':
        user = check_if_user_loggedin(request)
        form = RegisterNewTransactionFrom(request.POST or None)
        if form.is_valid():
            new_transaction = Transactions(
                transaction_type=form.cleaned_data['transaction_type'], amount=form.cleaned_data['amount'], category=form.cleaned_data['category'], source=form.cleaned_data['source'])
            new_transaction.user = user
            new_transaction.save()
            context = {'transaction': new_transaction}
            return render(request, 'partials/transaction.html', context)

    return render(request, 'partials/form.html', {'form': RegisterNewTransactionFrom()})


def vew_user_transactions(request):
    user = check_if_user_loggedin(request)
    context = {'transactions': Transactions.objects.filter(
        user=user).order_by('-id')}
    return render(request, "vew_transactions_template.html", context)
