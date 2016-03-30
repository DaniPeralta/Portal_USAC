from django.contrib import admin
from .models import Noticia, Experiencia, Pais, Anho, Universidad, Beca, T_Beca, Formulario, Datos_Beca

# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'publish')
	list_filter = ('created', 'publish')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'publish'
	ordering = ['publish']

class Datos_BecaAdmin(admin.ModelAdmin):

	list_display = ('nombre_completo', 'beca', 'beca_year', 'promedio')
	ordering = ['beca', 'promedio', 'nombre_completo']
	list_filter = ('beca', 'beca__course')

	def beca_year(self, obj):
		return obj.beca.course


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Experiencia)
admin.site.register(Pais)
admin.site.register(Anho)
admin.site.register(Universidad)
admin.site.register(Beca)
admin.site.register(T_Beca)
admin.site.register(Formulario)
admin.site.register(Datos_Beca, Datos_BecaAdmin)
