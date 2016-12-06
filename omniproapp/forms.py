from django import forms


class BaselineProfileForm(forms.Form):
    baseline_file = forms.FileField(
        label='Select a baseline file'
    )

class MeasuredProfileForm(forms.Form):
    measurement_file = forms.FileField(
        label='Select a measurement file'
    )