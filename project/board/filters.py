from django.forms import DateInput
from django_filters import FilterSet, ModelChoiceFilter, CharFilter, DateFilter, ChoiceFilter

from .category_type import CATEGORY_TYPE
from .models import Announcement
from django.utils.translation import gettext as _, gettext_lazy


# Создаем свой набор фильтров для модели Announcement.
class AnnouncementFilter(FilterSet):
    category = ChoiceFilter(choices=CATEGORY_TYPE,
                            label=gettext_lazy('Категория'),
                            empty_label=gettext_lazy('Категория не выбрана')
                            )

    title = CharFilter(lookup_expr='contains', )

    date = DateFilter(field_name='data',
                      lookup_expr='gt',
                      label=gettext_lazy('Дата'),
                      widget=DateInput(attrs={'type': 'date'}, )
                      )

    # class Meta:
    #     model = Announcement
    #     # В fields мы описываем по каким полям модели будет производиться фильтрация.
    #     fields = {
    #         # поиск по названию, категории и дате публикации
    #         # 'author': ['icontains'],
    #         'category': ['icontains'],
    #         'dateCreation': ['icontains'],
    #     }

    # category = ChoiceFilter(field_name='announcement__category',
    #                         queryset=Announcement.objects.all(),
    #                         label=gettext_lazy('Категория'),
    #                         empty_label=gettext_lazy('Категория не выбрана')
    #                         )
    # title = CharFilter(lookup_expr='contains', )
    #
    # date = DateFilter(field_name='data',
    #                   lookup_expr='gt',
    #                   label=gettext_lazy('Дата'),
    #                   widget=DateInput(attrs={'type': 'date'}, )
    #                   )
