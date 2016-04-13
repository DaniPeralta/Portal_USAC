from django.contrib import admin
from .models import Noticia, Experiencia, Pais, Anho, Universidad, Beca, T_Beca, Formulario, Datos_Beca, MasInfo

# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'publish')
	list_filter = ('created', 'publish')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'publish'
	ordering = ['publish']

class Datos_BecaAdmin(admin.ModelAdmin):

	list_display = ('nombre_completo', 'beca', 'beca_year', 'promedio', 'aceptado')
	ordering = ['beca', 'promedio', 'nombre_completo']
	list_filter = ('beca', 'beca__course', 'genero', 'edad', 'status', 'trabaja_ing')
	search_fields = ('n_carne', 'profesion', 'carrera')
	actions = ['cambiar_aceptado', 'cambiar_denegado']


	def beca_year(self, obj):
		return obj.beca.course

	def cambiar_aceptado(self, request, queryset):

		rows_updated = queryset.update(aceptado=True)

		if rows_updated == 1:
			message_bit = "1 estudiante fue actualizad"
		else:
			message_bit = "%s estudiantes fueron" % rows_updated

		self.message_user(request, "%s satisfactoriamente fueron actualizados." % message_bit)

	def cambiar_denegado(self, request, queryset):

		rows_updated = queryset.update(aceptado=False)

		if rows_updated == 1:
			message_bit = "1 estudiante fue actualizad"
		else:
			message_bit = "%s estudiantes fueron" % rows_updated

		self.message_user(request, "%s satisfactoriamente fueron actualizados." % message_bit)


class BecaAdmin(admin.ModelAdmin):

	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Experiencia)
admin.site.register(Pais)
admin.site.register(Anho)
admin.site.register(Universidad)
admin.site.register(Beca, BecaAdmin)
admin.site.register(T_Beca)
admin.site.register(Formulario)
admin.site.register(MasInfo)
admin.site.register(Datos_Beca, Datos_BecaAdmin)
