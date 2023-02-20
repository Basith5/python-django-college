from django import forms

class Feedback(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Email'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Phone Number'}))
    feedback = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Comment your feedback'}))