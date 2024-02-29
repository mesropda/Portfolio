from django.shortcuts import render
from django.contrib import messages
from .forms import RegisterNewTransactionFrom


from tracker.views import check_if_user_loggedin
from .models import Transactions

# Create your views here.


def user_home_page(request):
    context = {'form': RegisterNewTransactionFrom(),
               'transactions': Transactions.objects.all()}
    return render(request, "index.html", context)


def monthly_report(request):
    return render(request, "monthly-report.html", {})


def history(request):
    return render(request, "history.html", {})


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
