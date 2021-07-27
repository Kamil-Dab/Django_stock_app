from django import forms
from .models import StockQuery
from django.core.exceptions import ValidationError


class StockQueryForm(forms.ModelForm):
    start_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    end_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker2'
        })
    )

    class Meta:
        model = StockQuery
        fields = [
            'company_name',
            'start_date',
            'end_date'
        ]

    def clean(self):
        cd = self.cleaned_data

        start_date = cd.get("start_date")
        end_date = cd.get("end_date")

        if start_date > end_date:
            raise ValidationError("Start date should be earlier than end date")

        return cd
