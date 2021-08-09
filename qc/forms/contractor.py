from django import forms
from qc.models import Contact, Company


class ContactAddForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ['isvalid', 'addtime', 'updatetime']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'comp': forms.Select(attrs={'class': 'custom-select'}),
            'telprim': forms.TextInput(attrs={'class': 'form-control'}),
            'telscnd': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CompanyAddLessForm(forms.ModelForm):

    class Meta:
        model = Company
        exclude = ['isvalid', 'addtime', 'updatetime']
        widgets = {
            'cmpsn': forms.TextInput(attrs={'class': 'form-control'}),
            'cmpname': forms.TextInput(attrs={'class': 'form-control'}),
            'cmpsponsor': forms.Select(attrs={'class': 'form-control'}),
            'cmptel': forms.TextInput(attrs={'class': 'form-control'}),
            'cmpfax': forms.TextInput(attrs={'class': 'form-control'}),
            'cmpaddr': forms.TextInput(attrs={'class': 'form-control'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }