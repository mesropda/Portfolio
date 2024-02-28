from django.shortcuts import render
from django.contrib import messages
from .forms import RegisterNewTransactionFrom


from tracker.views import check_if_user_loggedin
from .models import Transactions

# Create your views here.


def user_home_page(request):
    # context = {'form': RegisterNewTransactionFrom()}
    # return render(request, 'index.html', context)
    return render(request, "index.html", {})


def monthly_report(request):
    return render(request, "monthly-report.html", {})


def history(request):
    return render(request, "history.html", {})


def add_expense(request):
    if request.method == 'POST':
        user = check_if_user_loggedin(request)
    return render(request, 'partials/form.html', {'form': RegisterNewTransactionFrom()})

    # if user.username == "edagmes":
    #     messages.success(
    #         request, "Your ae the admin user and cen't add en expense ")
    # else:
    #     new_transaction = Transactions()
