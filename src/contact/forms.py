from django import forms

from .models import Contact 

# class ContactForm(forms.ModelForm):
#     class Meta: 
#         model = Contact 
#         fields = [
#                 'email', 
#                 'subject', 
#                 'body' 
#                 ]
class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Your Email"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Subject"}))
    body = forms.CharField(
            widget=forms.Textarea(
                    attrs={
                        "rows": 20,
                        "cols": 120,
                        "placeholder":"Email Body"
                    }
                ) 
            )
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email") 
        return email 
