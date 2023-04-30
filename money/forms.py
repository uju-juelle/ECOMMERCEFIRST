from django import forms
from .models import *
SUBJECT_CHOICES =(
      ("Inquiry", "Inquiry"),
      ("Complaint", "Complaint")
   )
#METHOD ONE FOR REGULAR FORMS
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField(label="Your Email")
#     subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
#     message=forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"