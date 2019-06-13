from django.contrib.auth.models import User
from django import forms

class userForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_pass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    terms = forms.BooleanField(error_messages={'required': 'You must accept the terms and conditions'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email__iexact=email):
            raise forms.ValidationError('Email already exists')
        return email

    def clean_confirm_pass(self):
        password = self.cleaned_data['password']
        confirm_pass = self.cleaned_data['confirm_pass']

        if password != confirm_pass:
            raise forms.ValidationError("Passwords didn't match")
        return password

    """def clean_terms(self):
        if self.cleaned_data['terms'] != u'on':
            raise forms.ValidationError("You must agree to the terms&conditions")"""