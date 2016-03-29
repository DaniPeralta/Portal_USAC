from django.shortcuts import render, get_object_or_404
from .models import Noticia, Experiencia, Pais, Beca, T_Beca, Formulario, Datos_Beca
from .forms import Datos_BecaForm
from django.contrib import messages

# Prueba log
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def noticia_list(request):
	noticias = Noticia.objects.all()
	return render(request, 'noticias/noticia/list.html', {'noticias': noticias})


def noticia_lastest(request):
	noticias = Noticia.objects.all()
	return render(request, 'index.html', {'noticias': noticias})


def noticia_detail(request, year, noticia):
	noticia = get_object_or_404(Noticia, slug=noticia,
								publish__year=year)

	return render(request, 'noticias/noticia/detail.html', {'noticia': noticia})


def experiencia_list(request):
	experiencias = Pais.objects.all()
	return render(request, 'experiencia/experiences.html', {'experiencias': experiencias})


def beca_list(request):
	becas = T_Beca.objects.all()
	return render(request, 'becas/list.html', {'t_becas': becas})


def beca_form(request, id):
	beca = get_object_or_404(Beca, id=id)
	form = Datos_BecaForm(instance=beca)
	t_form = get_object_or_404(Formulario, beca=beca)
	campos = Formulario._meta.get_all_field_names()
	campos.remove('name_form')
	campos.remove('id')
	campos.remove('beca')

	# Almacenar datos del Formulario
	if request.method == 'POST':

		# Beca rellena
		beca_form = Datos_BecaForm(data=request.POST)

		if beca_form.is_valid():
			new_beca = beca_form.save(commit=False)
			# Asignamos la beca a los datos de la beca

			new_beca.beca = beca
			new_beca.save()
			messages.error(request, 'Po va bien')

		else:
			messages.error(request, 'Po va mal')
			messages.error(request, beca_form.errors.as_data())
	else:
		beca_form = Datos_BecaForm()

	return render(request, 'becas/apply.html', {'form': form, 'beca': beca, 't_form': t_form
												,'campos': campos, 'beca_form': beca_form})

