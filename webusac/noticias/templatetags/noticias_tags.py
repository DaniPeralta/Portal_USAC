from django import template

register = template.Library()

from ..models import Noticia

@register.simple_tag
def total_noticias():
	return Noticia.objects.count()

@register.inclusion_tag('noticias/noticia/lastest_noticias.html')
def show_lastest_noticias():
	slider = Noticia.objects.order_by('-publish')[:3]
	lastest_noticias = Noticia.objects.order_by('-publish')[3:6]
	return {'lastest_noticias': lastest_noticias, 'slider': slider}


# For concat variables in apply.html
@register.filter
def get_attribute(obj, name):
    return obj[name]

@register.filter
def get_attribute_label(obj, name):
	return obj[name].label


# Return the attribute of this field
@register.filter
def pr(dictionary, key):
	return getattr(dictionary, key)

@register.filter
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'required': 'required'})