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



@python_2_unicode_compatible
class Pais(models.Model):
	name = models.CharField(max_length=250)
	image = models.ImageField(upload_to='countries')

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class Universidad(models.Model):
	name = models.CharField(max_length=250)
	country = models.ForeignKey(Pais, related_name='universities')

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

	n_carne = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	n_colegiado = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	trabaja_ing = models.CharField(max_length=10,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),), default='no')

	n_reg_personal = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	unidad_trabajo = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	profesion = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	trabaja_usac = models.CharField(max_length=10,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),), default='no')

	trabaja_usac_lugar = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	carrera= models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	status = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	nombre_completo = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	telefono = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	email = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	edad = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	promedio = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	creditos = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	calusac = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	calusac_ult_niv = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	niv_ingl = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')

	nombre_curso_1 = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	secc_curso_1 = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	nombre_curso_2 = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	secc_curso_2 = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	laboratorio = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	escuela_vac_ant = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	escuela_vac_ant_curso = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	escuela_vac_ant_fecha = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	lugar_trabajo = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	salario = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	trabajo_padres = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	n_hermanos = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	zona_vive = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	departamento_vive = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	casa = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	apoyo_familiar = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	sosten_estudios = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	recibe_ayuda = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	transporte = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')

	conv_ant = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	conv_ant_cual = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	conv_ant_exp = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	beneficiado = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	anho = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	genero = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	dpi = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	pasaporte = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	exp_lab = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	estudios_completos = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	tit_acred = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	adjunto1 = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	adjunto2 = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')

	def __str__(self):
		return self.name_form

	def __unicode__(self):
		return unicode(self.name_form)
"""
@python_2_unicode_compatible
class Formulario(models.Model):
	"""' \
	Son demasiados atributos y con demasiados matices para ponerlos en ingles'' \
																			  '"""

	name_form = models.CharField(max_length=100)
	n_carne = models.BooleanField(default=False)
	n_colegiado = models.BooleanField(default=False)
	trabaja_ing = models.BooleanField(default=False)
	n_reg_personal = models.BooleanField(default=False)
	unidad_trabajo = models.BooleanField(default=False)
	profesion = models.BooleanField(default=False)
	trabaja_usac = models.BooleanField(default=False)
	trabaja_usac_lugar = models.BooleanField(default=False)
	carrera = models.BooleanField(default=False)
	status = models.BooleanField(default=False)
	nombre_completo = models.BooleanField(default=False)
	telefono = models.BooleanField(default=False)
	email = models.BooleanField(default=False)
	edad = models.BooleanField(default=False)
	promedio = models.BooleanField(default=False)
	creditos = models.BooleanField(default=False)
	calusac = models.BooleanField(default=False)
	calusac_ult_niv = models.BooleanField(default=False)
	niv_ingl = models.BooleanField(default=False)
	nombre_curso_1 = models.BooleanField(default=False)
	secc_curso_1 = models.BooleanField(default=False)
	nombre_curso_2 = models.BooleanField(default=False)
	secc_curso_2 = models.BooleanField(default=False)
	laboratorio = models.BooleanField(default=False)
	escuela_vac_ant = models.BooleanField(default=False)
	escuela_vac_ant_curso = models.BooleanField(default=False)
	escuela_vac_ant_fecha = models.BooleanField(default=False)
	lugar_trabajo = models.BooleanField(default=False)
	salario = models.BooleanField(default=False)
	trabajo_padres = models.BooleanField(default=False)
	n_hermanos = models.BooleanField(default=False)
	zona_vive = models.BooleanField(default=False)
	departamento_vive = models.BooleanField(default=False)
	casa = models.BooleanField(default=False)
	apoyo_familiar = models.BooleanField(default=False)
	sosten_estudios = models.BooleanField(default=False)
	recibe_ayuda = models.BooleanField(default=False)
	transporte = models.BooleanField(default=False)

	conv_ant = models.BooleanField(default=False)
	conv_ant_cual = models.BooleanField(default=False)
	conv_ant_exp = models.BooleanField(default=False)
	beneficiado = models.BooleanField(default=False)
	anho = models.BooleanField(default=False)
	genero = models.BooleanField(default=False)
	dpi = models.BooleanField(default=False)
	pasaporte = models.BooleanField(default=False)
	exp_lab = models.BooleanField(default=False)
	estudios_completos = models.BooleanField(default=False)
	tit_acred = models.BooleanField(default=False)
	adjunto1 = models.BooleanField(default=False)
	adjunto2 = models.BooleanField(default=False)

	def __str__(self):
		return self.name_form

	def __unicode__(self):
		return unicode(self.name_form)"""


@python_2_unicode_compatible
class Beca(models.Model):

	name = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	description = models.TextField()
	course = models.ForeignKey(Anho, related_name='becas')
	type = models.ForeignKey(T_Beca, related_name='becas')
	date_start = models.DateField()
	date_end = models.DateField()
	publish = models.DateTimeField(default=timezone.now)
	attach = models.FileField(upload_to='PDF')
	form = models.ForeignKey(Formulario, related_name='beca')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('beca_form',
					   args=[self.publish.year,
							 self.id,
							 self.slug])


@python_2_unicode_compatible
class Datos_Beca(models.Model):

	beca = models.ForeignKey(Beca, related_name="data")
	n_carne = models.PositiveIntegerField(blank=True, null=True)
	n_colegiado = models.PositiveIntegerField(blank=True, null=True)
	trabaja_ing = models.BooleanField(default=False, blank=True)
	n_reg_personal = models.PositiveIntegerField(blank=True, null=True)
	unidad_trabajo = models.CharField(max_length=300, blank=True)
	profesion = models.CharField(max_length=300, blank=True)
	trabaja_usac = models.BooleanField(default=False, blank=True)
	trabaja_usac_lugar = models.CharField(max_length=300, blank=True)
	carrera = models.CharField(max_length=50, blank=True,
							   choices=(('Ingeniería Civil', 'Ingeniería Civil'),
									    ('Ingeniería Quimica', 'Ingeniería Quimica'),
										('Ingeniería Industrial', 'Ingeniería Industrial'),
										('Ingeniería Eléctrica', 'Ingeniería Eléctrica'),
										('Ingeniería Mecánica', 'Ingeniería Mecánica'),
										('Ingeniería Mecánica Eléctrica', 'Ingeniería Mecánica Eléctrica'),
										('Ingeniería Mecánica Industrial', 'Ingeniería Mecánica Industrial'),
										('Ingeniería en Ciencias y Sistemas', 'Ingeniería en Ciencias y Sistemas'),
										('Ingeniería Electrónica', 'Ingeniería Electrónica'),
										('Ingeniería Ambiental', 'Ingeniería Ambiental'),
										('Otros', 'Otros'),
										))
	status = models.CharField(max_length=12, blank=True,
							  choices=(('estudiante', 'Estudiante'),
									   ('profesional', 'Profesional'),))
	nombre_completo = models.CharField(max_length=300, blank=True)
	telefono = models.CharField(max_length=300, blank=True)
	email = models.EmailField(blank=True)
	edad = models.PositiveIntegerField(blank=True, null=True)
	promedio = models.FloatField(blank=True, null=True)
	creditos = models.FloatField(blank=True, null=True)
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
	salario = models.FloatField(blank=True, null=True)
	trabajo_padres = models.CharField(max_length=300, blank=True)
	n_hermanos = models.PositiveSmallIntegerField(blank=True, null=True)
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

	conv_ant = models.CharField(max_length=2, blank=True,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),))
	conv_ant_cual = models.CharField(max_length=100, blank=True)
	conv_ant_exp = models.CharField(max_length=200, blank=True)
	beneficiado = models.CharField(max_length=2, blank=True,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),))
	anho = models.CharField(max_length=15, blank=True,
							  choices=(('Junio 2010', 'Junio 2010'),
									   ('Junio 2011', 'Junio 2011'),
									   ('Diciembre 2010', 'Diciembre 2010'),
									   ('Diciembre 2011', 'Diciembre 2011')
									   ))
	genero = models.CharField(max_length=9, blank=True,
							  choices=(('masculino', 'Masculino'),
									   ('femenino', 'Femenino'),))
	dpi = models.CharField(max_length=13, blank=True)
	pasaporte = models.CharField(max_length=20, blank=True)
	exp_lab = models.CharField(max_length=2, blank=True,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),))
	estudios_completos =  models.CharField(max_length=12, blank=True,
							  choices=(('licenciatura', 'Licenciatura'),
									   ('especialidad', 'Especialidad'),
									   ('maestría', 'Maestría'),
									   ('doctorado', 'Doctorado')
									   ))
	tit_acred = models.CharField(max_length=100, blank=True)
	adjunto1 = models.FileField(upload_to='Adjuntos_Beca', blank=True,)
	adjunto2 = models.FileField(upload_to='Adjuntos_Beca', blank=True,)
	aceptado = models.BooleanField(default=False)

	def __str__(self):
		return self.beca.name

	class Meta:
		unique_together = (("beca", "dpi"), ("beca", "n_carne"), ("beca", "n_colegiado"))

@python_2_unicode_compatible
class MasInfo(models.Model):

	name = models.CharField(max_length=250)
	adjunto = models.FileField(upload_to='MasInfo')

	def __str__(self):
		return self.name




