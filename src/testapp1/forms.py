from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your full name",
                "id": "form_full_name"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your email address"
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Your message"
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not "hotmail.de" in email:
            raise forms.ValidationError("Email has to be valid!")
        # elif not "gmail.com" in email:
        #     raise forms.ValidationError("Email has to be valid!")
        # elif not "hotmail.com" in email:
        #     raise forms.ValidationError("Email has to be valid!")

        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()