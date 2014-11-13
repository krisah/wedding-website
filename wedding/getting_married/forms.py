from django import forms

class ContactForm(forms.Form):
        first_name = forms.CharField(max_length=100)
        last_name = forms.CharField(max_length=100)
        message = forms.CharField(widget=forms.Textarea)
        email = forms.EmailField()
        cc_myself = forms.BooleanField(required=False)
