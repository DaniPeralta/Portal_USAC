from django.shortcuts import render, get_object_or_404
from .models import Noticia, Experiencia, Pais, Beca, T_Beca, Formulario
from .forms import Datos_BecaForm

# Create your views here.


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
	form = Datos_BecaForm()
	t_form = get_object_or_404(Formulario, beca=beca)
	campos = ["n_carne", "n_colegiado", "profesion", "edad"]
	return render(request, 'becas/apply.html', {'form': form, 'beca': beca, 't_form': t_form
												,'campos': campos})

