# import re
# from django import forms
# from django.contrib.auth.models import User
#
#
# class UserRegistrationForm(forms.Form):
#     username = forms.TextInput()
#     email = forms.EmailField(required=true)
#     password1 = forms.PasswordInput()
#     password2 = forms.PasswordInput()
#
#     def clean_username(self):
#         try:
#             user = User.objects.get(username__iexact=self.cleaned_data['username'])
#         except User.DoesNotExist:
#             return self.cleaned_data['username']
#         raise forms.ValidationError("Username already exists.")
#
#     def clean(self):
#         if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
#             if self.cleaned_data['password1'] != self.cleaned_data['password2']:
#                 raise forms.ValidationError("Passwords much match")
#         return self.cleaned_data
