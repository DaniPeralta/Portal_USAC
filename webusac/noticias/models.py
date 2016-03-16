# coding=utf-8
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.


@python_2_unicode_compatible
class Noticia(models.Model):

	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='images_upload/%Y/%m/%d',
							  blank=True, default='images_upload/logo2.png')


	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('noticias:noticia_detail',
					   args=[self.publish.year,
							 self.slug])



# Experiencias

@python_2_unicode_compatible
class Pais(models.Model):
	name = models.CharField(max_length=250)
	# Continent? Necessary?
	image = models.ImageField(upload_to='countries')

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class Universidad(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Anho(models.Model):
	year = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.year)


@python_2_unicode_compatible
class Experiencia(models.Model):
	name_student = models.CharField(max_length=250)
	experience = models.FileField(upload_to='experiences')
	country = models.ForeignKey(Pais, related_name='experiences')
	university = models.ForeignKey(Universidad, related_name='student')
	year = models.ForeignKey(Anho, related_name='experiences')
	thesis = models.FileField(upload_to='thesis')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name_student

	class Meta:
		ordering = ('-year',)


# Becas

@python_2_unicode_compatible
class T_Beca(models.Model):

	STATUS_CHOICES = (('nacional', 'Nacional'), ('internacional', 'Internacional'),)
	type = models.CharField(max_length=13, choices=STATUS_CHOICES,
							default='nacional')

	def __str__(self):
		return self.type



@python_2_unicode_compatible
class Formulario(models.Model):
	"""Son demasiados atributos y con demasiados matices para ponerlos en ingles"""

	name_form = models.CharField(max_length=100)
	n_carne = models.BooleanField(default=True)
	n_colegiado = models.BooleanField(default=True)
	trabaja_ing = models.BooleanField(default=True)
	n_reg_personal = models.BooleanField(default=True)
	unidad_trabajo = models.BooleanField(default=True)
	profesion = models.BooleanField(default=True)
	trabaja_usac = models.BooleanField(default=True)
	trabaja_usac_lugar = models.BooleanField(default=True)
	carrera = models.BooleanField(default=True)
	status = models.BooleanField(default=True)
	nombre_completo = models.BooleanField(default=True)
	telefono = models.BooleanField(default=True)
	email = models.BooleanField(default=True)
	edad = models.BooleanField(default=True)
	promedio = models.BooleanField(default=True)
	creditos = models.BooleanField(default=True)
	calusac = models.BooleanField(default=True)
	calusac_ult_niv = models.BooleanField(default=True)
	niv_ingl = models.BooleanField(default=True)
	nombre_curso_1 = models.BooleanField(default=True)
	secc_curso_1 = models.BooleanField(default=True)
	nombre_curso_2 = models.BooleanField(default=True)
	secc_curso_2 = models.BooleanField(default=True)
	laboratorio = models.BooleanField(default=True)
	escuela_vac_ant = models.BooleanField(default=True)
	escuela_vac_ant_curso = models.BooleanField(default=True)
	escuela_vac_ant_fecha = models.BooleanField(default=True)
	lugar_trabajo = models.BooleanField(default=True)
	salario = models.BooleanField(default=True)
	trabajo_padres = models.BooleanField(default=True)
	n_hermanos = models.BooleanField(default=True)
	zona_vive = models.BooleanField(default=True)
	departamento_vive = models.BooleanField(default=True)
	casa = models.BooleanField(default=True)
	apoyo_familiar = models.BooleanField(default=True)
	sosten_estudios = models.BooleanField(default=True)
	recibe_ayuda = models.BooleanField(default=True)
	transporte = models.BooleanField(default=True)

	def __str__(self):
		return self.name_form

	def __unicode__(self):
		return unicode(self.name_form)


@python_2_unicode_compatible
class Beca(models.Model):

	name = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250)
	description = models.TextField()
	course = models.ForeignKey(Anho, related_name='becas')
	type = models.ForeignKey(T_Beca, related_name='becas')
	date_start = models.DateField()
	date_end = models.DateField()
	attach = models.FileField(upload_to='PDF')
	form = models.ForeignKey(Formulario, related_name='beca')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('beca_form',
					   args=[self.id])


@python_2_unicode_compatible
class Datos_Beca(models.Model):

	beca = models.OneToOneField(Beca, related_name="data")
	n_carne = models.PositiveIntegerField(blank=True)
	n_colegiado = models.PositiveIntegerField(blank=True)
	trabaja_ing = models.BooleanField(default=False, blank=True)
	n_reg_personal = models.PositiveIntegerField(blank=True)
	unidad_trabajo = models.CharField(max_length=300, blank=True)
	profesion = models.CharField(max_length=300, blank=True)
	trabaja_usac = models.BooleanField(default=False, blank=True)
	trabaja_usac_lugar = models.CharField(max_length=300, blank=True)
	carrera = models.CharField(max_length=300, blank=True)
	status = models.CharField(max_length=12, blank=True,
							  choices=(('estudiante', 'Estudiante'),
									   ('profesional', 'Profesional'),))
	nombre_completo = models.CharField(max_length=300, blank=True)
	telefono = models.CharField(max_length=300, blank=True)
	email = models.EmailField(blank=True)
	edad = models.PositiveIntegerField(blank=True)
	promedio = models.FloatField(blank=True)
	creditos = models.FloatField(blank=True)
	calusac = models.CharField(max_length=2, blank=True,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),))
	calusac_ult_niv = models.CharField(max_length=100, blank=True)
	niv_ingl = models.CharField(max_length=10, blank=True,
							  choices=(('basico', 'Básico'),
									   ('medio', 'Medio'),
									   ('avanzado', 'Avanzado'),))
	nombre_curso_1 = models.CharField(max_length=300, blank=True)
	secc_curso_1 = models.CharField(max_length=300, blank=True)
	nombre_curso_2 = models.CharField(max_length=300, blank=True)
	secc_curso_2 = models.CharField(max_length=300, blank=True)
	laboratorio = models.CharField(max_length=2, blank=True,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),))
	escuela_vac_ant = models.CharField(max_length=2, blank=True,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),))
	escuela_vac_ant_curso = models.CharField(max_length=100, blank=True)
	escuela_vac_ant_fecha = models.CharField(max_length=10, blank=True)
	lugar_trabajo = models.CharField(max_length=100, blank=True)
	salario = models.FloatField(blank=True)
	trabajo_padres = models.CharField(max_length=300, blank=True)
	n_hermanos = models.PositiveSmallIntegerField(blank=True)
	zona_vive = models.CharField(max_length=100, blank=True)
	departamento_vive = models.CharField(max_length=200, blank=True)
	casa = models.CharField(max_length=20, blank=True,
							  choices=(('propia', 'Propia'),
									   ('alquilada', 'Alquilada'),
									   ('casa de huespedes', 'Casa de Huéspedes'),
									   ('de familiares', 'De Familiares'),))
	apoyo_familiar = models.CharField(max_length=100, blank=True)
	sosten_estudios = models.CharField(max_length=100, blank=True)
	recibe_ayuda = models.CharField(max_length=100, blank=True)
	transporte = models.CharField(max_length=20, blank=True,
							  choices=(('vehiculo', 'Vehiculo'),
									   ('bus', 'Bus'),
									   ('moto', 'Moto'),
									   ('a pie', 'A Pie'),))

	def __str__(self):
		return self.beca






