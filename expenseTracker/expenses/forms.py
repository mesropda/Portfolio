from django import forms
from .models import Transactions


EXPENSE_CATEGORY_CHOICES = (
    ("House", "House"),
    ("Food", "Food"),
    ("Transport", "Transport"),
    ("Shopping", "Shopping"),
    ("Necessities", "Necessities"),
    ("Bills", "Bills"),
    ("Leisure", "Leisure"),
    ("Other", "Other")
)

SOURCE_CHOICES = (
    ("My account", "My account"),
    ("Salary", "Salary"),
    ("Gov_Social", "Gov_Social"),
    ("Business_Profit", "Business_Profit"),
    ("Other", "Other")
)

TRANSACTION_CHOICES = (
    ("Deposit", "Deposit"),
    ("Withdrawal", "Withdrawal"),
)


class RegisterNewTransactionFrom(forms.ModelForm):
    transaction_type = forms.ChoiceField(choices=TRANSACTION_CHOICES, widget=forms.Select(
        attrs={'class': 'form_input_register'}))
    amount = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Enter Sum', 'class': 'form_input_register'}))
    category = forms.ChoiceField(choices=EXPENSE_CATEGORY_CHOICES, widget=forms.Select(
        attrs={'class': 'form_input_register'}))
    source = forms.ChoiceField(choices=SOURCE_CHOICES, widget=forms.Select(
        attrs={'class': 'form_input_register'}))

    class Meta:
        model = Transactions
        fields = ('transaction_type', 'amount', 'category', 'source')


# class TransactionFilterForm(forms.Form):
#     transaction_type = forms.ChoiceField(choices=TRANSACTION_CHOICES, widget=forms.Select(
#         attrs={'class': 'form_input_register'}))
