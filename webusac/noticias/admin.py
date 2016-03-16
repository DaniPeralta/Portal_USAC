from django.contrib import admin
from .models import Noticia, Experiencia, Pais, Anho, Universidad, Beca, T_Beca, Formulario

# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'publish')
	list_filter = ('created', 'publish')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'publish'
	ordering = ['publish']

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Experiencia)
admin.site.register(Pais)
admin.site.register(Anho)
admin.site.register(Universidad)
admin.site.register(Beca)
admin.site.register(T_Beca)
admin.site.register(Formulario)