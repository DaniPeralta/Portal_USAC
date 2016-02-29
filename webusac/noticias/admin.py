from django.contrib import admin
from .models import Noticia

# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'publish')
	list_filter = ('created', 'publish')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'publish'
	ordering = ['publish']

admin.site.register(Noticia, NoticiaAdmin)