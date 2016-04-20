# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db import IntegrityError

from .models import Noticia, MasInfo, Pais, Beca, T_Beca, Formulario
from .forms import Datos_BecaForm
from django.contrib import messages
from django.core.mail import send_mail

# Para poder mandar los email sin problemas unicode.
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def noticia_list(request):
	noticias_list = Noticia.objects.all()
	paginator = Paginator(noticias_list, 9) # 9 news for page
	page = request.GET.get('page')
	try:
		noticias = paginator.page(page)
	except PageNotAnInteger:
		# First page
		noticias = paginator.page(1)
	except EmptyPage:
		# Last page
		noticias = paginator.page(paginator.num_pages)

	return render(request, 'noticias/noticia/list.html', {'noticias': noticias, 'page': page})


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

def masinfo_list(request):
	masinfo = MasInfo.objects.all()
	return render(request, 'moreinfo/moreinfo.html', {'masinfo': masinfo})

def beca_list(request):
	# Todos los tipos de beca que existen
	becas = T_Beca.objects.all()
	date = timezone.datetime.now().date()

	return render(request, 'becas/list.html', {'t_becas': becas, 'date': date})


def beca_form(request,id, year, slug):
	beca = get_object_or_404(Beca, id=id)
	form = Datos_BecaForm(instance=beca)
	t_form = get_object_or_404(Formulario, beca=beca)
	campos2 = Formulario._meta.get_fields()

	campos = []
	for camp in campos2:
		campos += [camp.name]

	campos.remove('name_form')
	campos.remove('id')
	campos.remove('beca')

	# messages.error(request, timezone.datetime.now().date())

	# Almacenar datos del Formulario
	if request.method == 'POST':

		# Beca rellena
		beca_form = Datos_BecaForm(data=request.POST)

		if beca_form.is_valid():
			if beca.date_end < timezone.now().date():
				messages.error(request, "Plazo de beca terminado")
			else:

				new_beca = beca_form.save(commit=False)
				# Asignamos la beca a los datos de la beca

				new_beca.beca = beca

				try:
					cd = beca_form.cleaned_data
					subject = 'Registrado correctamente en la beca: "'+beca.name+'"'
					message = 'Usted se ha registrado con éxito en la beca "' + beca.name + \
							  '"\n\n\n Gracias por su participación. Pronto se conocerá el resultado.\n\n' \
							  'Universidad San Carlos de Guatemala. Facultad de Ingenería.'

					new_beca.save()
					messages.success(request, 'Registrado Correctamente')
					try:
						send_mail(subject,
								  message,
								  'dani.peralta.de@gmail.com', [cd['email']])
					except Exception as e:
						messages.error(request, 'Error en el envío del mail')
						#messages.error(request, e)

				except IntegrityError:
					#messages.error(request, beca_form.errors.as_data())
					messages.error(request, 'Usted ya está registrado en la beca')
		else:
			messages.error(request, 'Error mostrando el formulario')
			#messages.error(request, beca_form.errors.as_data())
	else:
		beca_form = Datos_BecaForm()

	return render(request, 'becas/apply.html', {'form': form, 'beca': beca, 't_form': t_form
												,'campos': campos, 'beca_form': beca_form})

