from django.shortcuts import render, get_object_or_404
from .models import Noticia, Experiencia, Pais, Beca, T_Beca
from .forms import ApplyForm

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

def forms(request):
	form = ApplyForm()
	return render(request, 'becas/apply.html', {'form': form})

