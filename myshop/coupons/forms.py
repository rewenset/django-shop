from django import forms


class CouponsApplyForm(forms.Form):
    code = forms.CharField()
