from django.forms import ModelForm
from backend.models import Complaint

class ComplaintForm(ModelForm):
    class Meta:
        model=Complaint
        fields=['Title','Type_of_complaint','Description']