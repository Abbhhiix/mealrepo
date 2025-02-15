from django import forms
from .models import UserBudget

class UserBudgetForm(forms.ModelForm):
    class Meta:
        model = UserBudget
        fields = ['budget', 'dietary_preference']
#budget
class BudgetForm(forms.ModelForm):
    class Meta:
        model = UserBudget
        fields = ['budget', 'dietary_preference']
