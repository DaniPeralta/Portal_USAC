from django.conf.urls import url
from . import views

urlpatterns = [
	# noticias views
	# Index
	#url(r'^$', views.noticia_list, name='noticia_list'),
	# Noticias list
	url(r'^$', views.noticia_list, name='noticia_list'),
	# One Noticia
	url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<noticia>[-\w]+)/$',
		views.noticia_detail, name='noticia_detail'),
]

