from django import forms
from .models import Datos_Beca

""" Antigua manera de hacerlo

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
"""

class Datos_BecaForm(forms.ModelForm):
	class Meta:
		model = Datos_Beca
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(Datos_BecaForm, self).__init__(*args, **kwargs)
		# Para que nos deje validar el formulario
		self.fields['beca'].required = False

