from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Full Name')
    email = forms.EmailField(label='Email Address')
    message = forms.CharField(widget=forms.Textarea, label="Enter Message")



    #def send_email(self):
        #send email using the self.cleaned_data dictionary
    #    pass
