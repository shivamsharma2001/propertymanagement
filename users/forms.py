from django import forms
from users.models import User

class UserSignUpForm(forms.Form):
    #password2 = forms.CharField(widget=forms.PasswordInput)

    class meta:
        model=User
        fields= ('first_name','last_name','email','mobile','password','password2')

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        try:
            CustomUser.objects.get(email__iexact=email)
            raise forms.ValidationError('email already exists')
        except CustomUser.DoesNotExist:
            return email

    def clean_password2(self):
        pw1 = self.cleaned_data.get('password1')
        pw2 = self.cleaned_data.get('password2')
        if pw1 and pw2 and pw1 == pw2:
            return pw2
        raise forms.ValidationError("passwords don't match")
