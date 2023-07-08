from django import forms
from .models import PointModel

class PointModelForm(forms.ModelForm):
    class Meta:
        model = PointModel
        fields = ["point","duedate","songmodel"]
        widgets = {
            'duedate': forms.DateInput(attrs={'type': 'date'})
        }

