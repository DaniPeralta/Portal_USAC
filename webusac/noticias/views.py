from django.shortcuts import render, get_object_or_404
from .models import Noticia

# Create your views here.

def noticia_list(request):
	noticias = Noticia.objects.all()
	return render(request, 'noticias/noticia/list.html', {'noticias': noticias})

def noticia_detail(request, year, month, day, noticia):
	noticia = get_object_or_404(Noticia, slug=noticia,
								publish__year = year,
								publish__month=month,
								publish__day=day)
	return render(request, 'noticias/noticia/detail.html', {'noticia':noticia})