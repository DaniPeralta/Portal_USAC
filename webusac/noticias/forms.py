from django import forms

class ApplyForm(forms.Form):
	name = forms.CharField(max_length=250)
	carnet_number = forms.IntegerField()
	degree = forms.CharField(max_length=200)
	phone = forms.IntegerField()
	email = forms.EmailField()
	unity = forms.BooleanField()
	average = forms.FloatField()
	credit = forms.FloatField()
	notes = forms.CharField(max_length=400)