from django.contrib.auth.forms import UserCreationForm
from .models import Account

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'username', 'employeeId', 'phone', 'department', 'password1', 'password2']
