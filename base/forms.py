from base.models import Comment, EnrollCourse
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("full_name", "email", "website", "message")


class EnrollNowForm(forms.ModelForm):
    class Meta:
        model = EnrollCourse
        fields = ("full_name", "email", "phone_number")

    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"]
        if len(full_name) < 3:
            raise forms.ValidationError("Full name must be at least 3 characters long.")
        return full_name

    def clean_email(self):
        email = self.cleaned_data["email"]
        from django.core.validators import EmailValidator

        email_validator = EmailValidator("Enter a valid email address.")
        email_validator(email)
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        import re

        if not re.match(r"^\+?1?\d{9,15}$", phone_number):
            raise forms.ValidationError("Enter a valid phone number.")
        return phone_number

    def __init__(self, *args, **kwargs):
        super(EnrollNowForm, self).__init__(*args, **kwargs)

        self.fields["full_name"].widget.attrs["placeholder"] = "Full Name"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["phone_number"].widget.attrs["placeholder"] = "Phone Number"
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
