from datetime import datetime

from django import template


register = template.Library()


@register.simple_tag()
def current_time(format_string='%d %b %Y'):
    return datetime.utcnow().strftime(format_string)


@register.simple_tag(takes_context=True)  #Параметр декоратора takes_context=True сообщает Django, что для работы тега требуется передать контекст.
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()  # нам позволяет скопировать все параметры текущего запроса.
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()
