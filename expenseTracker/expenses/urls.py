from django.urls import path
from .views import user_home_page, monthly_report, history, add_expense

app_name = "expenses"
urlpatterns = [

    path('index', user_home_page, name='index'),
    path('monthly-report', monthly_report, name='monthly'),
    path('history', history, name='history'),
    path('add-expense/', add_expense, name='add-expense'),

]
