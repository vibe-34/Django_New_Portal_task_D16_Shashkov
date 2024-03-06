from django.forms import DateInput
from django_filters import FilterSet, ModelChoiceFilter, CharFilter, DateFilter
from .models import Announcement
from django.utils.translation import gettext as _, gettext_lazy


# Создаем свой набор фильтров для модели Announcement.
# FilterSet, который мы наследуем, должен чем-то напомнить знакомые вам Django дженерики.
class AnnouncementFilter(FilterSet):
    class Meta:
        # В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        model = Announcement
        # В fields мы описываем по каким полям модели будет производиться фильтрация.
        fields = {
            # поиск по названию, категории и дате публикации
            # 'username': ['icontains'],
            'category': ['icontains'],
            'dateCreation': ['icontains'],
        }
