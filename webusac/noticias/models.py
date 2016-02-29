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
	image = models.ImageField(upload_to='webusac/noticias/static/noticias/images/%Y/%m/%d',
							  blank=True)

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('noticias:noticia_detail',
					   args=[self.publish.year,
							 self.publish.strftime('%m'),
							 self.publish.strftime('%d'),
							 self.slug])
