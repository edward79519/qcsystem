from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

from core.models import Employee


class EmployeeCreationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'password'},
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'password'}
        ),
    )
    error_messages = {
        'password_mismatch': '兩組密碼不合。',
    }

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'username': {
                'unique': '帳號已經重複，請更換下一個帳號。',
            },
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號:",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class ChangePWDForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='舊密碼',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'old-password'})
    )
    new_password1 = forms.CharField(
        label='新密碼:',
        widget=forms.PasswordInput(attrs={'autocomplete': 'old-password', 'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        label='確認密碼：',
        widget=forms.PasswordInput(attrs={'autocomplete': 'old-password', 'class': 'form-control'})
    )

    def clean_old_password(self):
        try:
            return super(ChangePWDForm, self).clean_old_password()
        except forms.ValidationError:
            raise forms.ValidationError("error")


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'email': 'E-mail',
            'first_name': '名字',
            'last_name': '姓氏',
        }



class EmployeeUpdateForm(forms.ModelForm):

    class Meta:
        model = Employee
        exclude = ['user']
        widgets = {
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'ext': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'tel': '電話',
            'ext': '分機',
            'department': '部門',
        }
