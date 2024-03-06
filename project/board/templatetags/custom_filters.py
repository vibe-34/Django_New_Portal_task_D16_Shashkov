from django import template

register = template.Library()

CATEGOR = {
        'Танки': 'TN',
        'Хилы': 'HL',
        'ДД': 'DD',
        'Торговцы': 'MA',
        'Гилдмастеры': 'GM',
        'Квестгиверы': 'GI',
        'Кузнецы': 'BS',
        'Кожевники': 'TA',
        'Зельевары': 'PB',
        'Мастера заклинаний': 'SM',
}


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def currency(value, code='Мастера заклинаний'):
    """
    value: значение, к которому нужно применить фильтр
    code: код категории
    """

    postfix = CATEGOR[code]
    # Возвращаемое функцией значение подставится в шаблон.
    return f'{value} {postfix}'
