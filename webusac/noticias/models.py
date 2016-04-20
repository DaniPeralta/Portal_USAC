# coding=utf-8
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.


@python_2_unicode_compatible
class Noticia(models.Model):

	title = models.CharField('Título', max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	body = models.TextField('Cuerpo')
	publish = models.DateTimeField('Publicado',default=timezone.now)
	created = models.DateTimeField('Creado', auto_now_add=True)
	updated = models.DateTimeField('Actualizado', auto_now_add=True)
	image = models.ImageField('Imagen', upload_to='images_upload/%Y/%m/%d',
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
	name = models.CharField('Nombre', max_length=250)
	image = models.ImageField('Imagen', upload_to='countries')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = ("País")
		verbose_name_plural = ("Países")



@python_2_unicode_compatible
class Universidad(models.Model):
	name = models.CharField('Nombre', max_length=250)
	country = models.ForeignKey(Pais, related_name='universities', verbose_name='País')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = ("Universidad")
		verbose_name_plural = ("Universidades")


@python_2_unicode_compatible
class Anho(models.Model):

	year = models.IntegerField('Año')

	def __str__(self):
		return '{}'.format(self.year)

	class Meta:
		verbose_name = ("Año")


@python_2_unicode_compatible
class Experiencia(models.Model):
	name_student = models.CharField('Nombre de estudiante', max_length=250)
	experience = models.FileField('Experiencia', upload_to='experiences')
	country = models.ForeignKey(Pais, related_name='experiences', verbose_name='País')
	university = models.ForeignKey(Universidad, related_name='student', verbose_name='Universidad')
	year = models.ForeignKey(Anho, related_name='experiences', verbose_name='Año')
	thesis = models.FileField('Tesis', upload_to='thesis')
	created = models.DateTimeField('Creado', auto_now_add=True)
	updated = models.DateTimeField('Modificado', auto_now_add=True)

	def __str__(self):
		return self.name_student

	class Meta:
		ordering = ('-year',)


# Becas

@python_2_unicode_compatible
class T_Beca(models.Model):

	STATUS_CHOICES = (('nacional', 'Nacional'), ('internacional', 'Internacional'),)
	type = models.CharField('Ámbito de la beca', max_length=13, choices=STATUS_CHOICES,
							default='nacional')

	def __str__(self):
		return self.type

	class Meta:
		verbose_name = ("Tipo Beca")
		verbose_name_plural = ("Tipo Beca")


@python_2_unicode_compatible
class Formulario(models.Model):
	"""Son demasiados atributos y con demasiados matices para ponerlos en ingles"""

	name_form = models.CharField('Nombre del formulario', max_length=100)

	n_carne = models.CharField('Nº carnet', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	n_colegiado = models.CharField('Nº colegiado', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	trabaja_ing = models.CharField('¿Trabaja en Ingeniería?', max_length=10,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),), default='no')

	n_reg_personal = models.CharField('Nº registro personal',max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	unidad_trabajo = models.CharField('Unidad de trabajo', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	profesion = models.CharField('Profesión', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	trabaja_usac = models.CharField('¿Trabaja en USAC?',max_length=10,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),), default='no')

	trabaja_usac_lugar = models.CharField('Si trabaja en la USAC, ¿Dónde?',max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	carrera = models.CharField('Carrera', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	status = models.CharField('Status', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	nombre_completo = models.CharField('Nombre Completo',max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	telefono = models.CharField('Teléfono', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	email = models.CharField('E-mail', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='requerido')
	edad = models.CharField('Edad', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	promedio = models.CharField('Promedio', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	creditos = models.CharField('Créditos', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	calusac = models.CharField('¿Ha estudiado en CALUSAC?', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	calusac_ult_niv = models.CharField('Nivel CALUSAC', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	niv_ingl = models.CharField('Nivel de inglés fuera de CALUSAC', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')

	nombre_curso_1 = models.CharField('Nombre del curso 1', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	secc_curso_1 = models.CharField('Sección del curso 1', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	nombre_curso_2 = models.CharField('Nombre del curso 2', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	secc_curso_2 = models.CharField('Sección del curso 2', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	laboratorio = models.CharField('¿Su curso lleva Laboratorio', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	escuela_vac_ant = models.CharField('Ha solicitado anteriormente escuela de vacaciones', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	escuela_vac_ant_curso = models.CharField('Si es positiva la respuesta, ¿En qué curso se le otorgó la beca', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	escuela_vac_ant_fecha = models.CharField('En que fecha se otorgó la beca', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	lugar_trabajo = models.CharField('Lugar de trabajo', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	salario = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	trabajo_padres = models.CharField('¿En qué trabajan los padres', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	n_hermanos = models.CharField('Nº de hermanos', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	zona_vive = models.CharField('En que zona vive', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	departamento_vive = models.CharField('En que departamento vive', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	casa = models.CharField('Su casa es:', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	apoyo_familiar = models.CharField('¿Quiénes apoyan al ingreso familiar?', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	sosten_estudios = models.CharField('¿Quién sostiene sus estudios?', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	recibe_ayuda = models.CharField('¿Recibe alguna ayuda económica extra?', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	transporte = models.CharField('Transporte a la universidad', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')

	conv_ant = models.CharField('Ha participado en convocatorias anteriores', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	conv_ant_cual = models.CharField('Indicar cuales (Si aplica):', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	conv_ant_exp = models.CharField('Explicar en que consistia:', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	beneficiado = models.CharField('Fue beneficiad@', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	anho = models.CharField('Año', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	genero = models.CharField('Género', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	dpi = models.CharField('Nº DPI', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='requerido')
	pasaporte = models.CharField('Nº Pasaporte', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	exp_lab = models.CharField('Posee experiencia laboral', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	estudios_completos = models.CharField('Estudios completos de:', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	tit_acred = models.CharField('Título que acredita', max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	adjunto1 = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')
	adjunto2 = models.CharField(max_length=10, choices=(('requerido', 'Requerido'), ('opcional', 'Opcional'), ('no', 'No'),), default='no')

	def __str__(self):
		return self.name_form

	def __unicode__(self):
		return unicode(self.name_form)


@python_2_unicode_compatible
class Beca(models.Model):

	name = models.CharField('Nombre de la beca', max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	description = models.TextField('Descripción')
	course = models.ForeignKey(Anho, related_name='becas', verbose_name='Curso')
	type = models.ForeignKey(T_Beca, related_name='becas', verbose_name='Tipo de beca')
	date_start = models.DateField('Fecha de inicio de la convocatoria')
	date_end = models.DateField('Fecha de fin de la convocatoria')
	publish = models.DateTimeField('Publicado', default=timezone.now)
	attach = models.FileField('Documento adjunto', upload_to='PDF')
	form = models.ForeignKey(Formulario, related_name='beca', verbose_name='Formulario')

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
	n_carne = models.PositiveIntegerField('Nº carné', blank=True, null=True)
	n_colegiado = models.PositiveIntegerField('Nº colegido', blank=True, null=True)
	trabaja_ing = models.BooleanField('¿Trabaja en Ingeniería?', default=False, blank=True)
	n_reg_personal = models.PositiveIntegerField('Nº registro personal', blank=True, null=True)
	unidad_trabajo = models.CharField('Unidad de trabajo', max_length=300, blank=True)
	profesion = models.CharField('Profesión', max_length=300, blank=True)
	trabaja_usac = models.BooleanField('¿Trabaja en USAC?', default=False, blank=True)
	trabaja_usac_lugar = models.CharField('Si trabaja en la USAC, ¿Dónde?', max_length=300, blank=True)
	carrera = models.CharField('Carrera', max_length=50, blank=True,
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
	telefono = models.PositiveIntegerField('Teléfono', blank=True, null=True)
	email = models.EmailField('E-mail', blank=True)
	edad = models.PositiveIntegerField(blank=True, null=True)
	promedio = models.FloatField(blank=True, null=True)
	creditos = models.FloatField('Créditos', blank=True, null=True)
	calusac = models.CharField('¿Ha estudiado en CALUSAC?', max_length=2, blank=True,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),))
	calusac_ult_niv = models.CharField('Nivel CALUSAC', max_length=100, blank=True)
	niv_ingl = models.CharField('Nivel de inglés fuera de CALUSAC', max_length=10, blank=True,
							  choices=(('basico', 'Básico'),
									   ('medio', 'Medio'),
									   ('avanzado', 'Avanzado'),))
	nombre_curso_1 = models.CharField('Nombre del curso 1', max_length=300, blank=True)
	secc_curso_1 = models.CharField('Sección del curso 1', max_length=300, blank=True)
	nombre_curso_2 = models.CharField('Nombre del curso 2', max_length=300, blank=True)
	secc_curso_2 = models.CharField('Sección del curso 2', max_length=300, blank=True)
	laboratorio = models.CharField('¿Su curso lleva Laboratorio', max_length=2, blank=True,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),))
	escuela_vac_ant = models.CharField('Ha solicitado anteriormente escuela de vacaciones', max_length=2, blank=True,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),))
	escuela_vac_ant_curso = models.CharField('Si es positiva la respuesta, ¿En qué curso se le otorgó la beca', max_length=100, blank=True)
	escuela_vac_ant_fecha = models.CharField('En que fecha se otorgó la beca', max_length=10, blank=True)
	lugar_trabajo = models.CharField('Lugar de trabajo', max_length=100, blank=True)
	salario = models.FloatField(blank=True, null=True)
	trabajo_padres = models.CharField('¿En qué trabajan los padres', max_length=300, blank=True)
	n_hermanos = models.PositiveSmallIntegerField('Nº de hermanos', blank=True, null=True)
	zona_vive = models.CharField('En que zona vive', max_length=100, blank=True)
	departamento_vive = models.CharField('En que departamento vive', max_length=200, blank=True)
	casa = models.CharField('Su casa es:', max_length=20, blank=True,
							  choices=(('propia', 'Propia'),
									   ('alquilada', 'Alquilada'),
									   ('casa de huespedes', 'Casa de Huéspedes'),
									   ('de familiares', 'De Familiares'),))
	apoyo_familiar = models.CharField('¿Quiénes apoyan al ingreso familiar?', max_length=100, blank=True)
	sosten_estudios = models.CharField('¿Quién sostiene sus estudios?', max_length=100, blank=True)
	recibe_ayuda = models.CharField('¿Recibe alguna ayuda económica extra?', max_length=100, blank=True)
	transporte = models.CharField('Transporte a la universidad', max_length=20, blank=True,
							  choices=(('vehiculo', 'Vehiculo'),
									   ('bus', 'Bus'),
									   ('moto', 'Moto'),
									   ('a pie', 'A Pie'),))

	conv_ant = models.CharField('Ha participado en convocatorias anteriores', max_length=2, blank=True,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),))
	conv_ant_cual = models.CharField('Indicar cuales (Si aplica):', max_length=100, blank=True)
	conv_ant_exp = models.CharField('Explicar en que consistia:', max_length=200, blank=True)
	beneficiado = models.CharField('Fue beneficiad@', max_length=2, blank=True,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),))
	anho = models.CharField('Año', max_length=15, blank=True,
							  choices=(('Junio 2010', 'Junio 2010'),
									   ('Junio 2011', 'Junio 2011'),
									   ('Diciembre 2010', 'Diciembre 2010'),
									   ('Diciembre 2011', 'Diciembre 2011')
									   ))
	genero = models.CharField('Género', max_length=9, blank=True,
							  choices=(('masculino', 'Masculino'),
									   ('femenino', 'Femenino'),))
	dpi = models.CharField('Nº DPI', max_length=13, blank=False)
	pasaporte = models.CharField('Nº Pasaporte', max_length=20, blank=True)
	exp_lab = models.CharField('Posee experiencia laboral', max_length=2, blank=True,
							  choices=(('si', 'Sí'),
									   ('no', 'No'),))
	estudios_completos =  models.CharField('Estudios completos de:', max_length=12, blank=True,
							  choices=(('licenciatura', 'Licenciatura'),
									   ('especialidad', 'Especialidad'),
									   ('maestría', 'Maestría'),
									   ('doctorado', 'Doctorado')
									   ))
	tit_acred = models.CharField('Título que acredita', max_length=100, blank=True)
	adjunto1 = models.FileField(upload_to='Adjuntos_Beca', blank=True,)
	adjunto2 = models.FileField(upload_to='Adjuntos_Beca', blank=True,)
	aceptado = models.BooleanField(default=False)


	def save(self, force_insert=False, force_update=False):
		self.nombre_completo = self.nombre_completo.upper()
		super(Datos_Beca, self).save(force_insert, force_update)

	def __str__(self):
		return self.beca.name

	class Meta:
		unique_together = (("beca", "dpi"))
		verbose_name = ("Datos de las Becas")
		verbose_name_plural = ("Datos de las Becas")


@python_2_unicode_compatible
class MasInfo(models.Model):

	name = models.CharField('Nombre', max_length=250)
	adjunto = models.FileField(upload_to='MasInfo')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = ("Más Info")
		verbose_name_plural = ("Más Info")





