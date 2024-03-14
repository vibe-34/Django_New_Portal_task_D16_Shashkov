from django_filters import FilterSet

from board.models import UserResponse, Announcement


class AnnouncementFilter(FilterSet):  # Берем все отзывы и фильтруем по объявлениям которые принадлежат текущему авторизованному пользователю

    class Meta:
        model = UserResponse
        fields = [
            'adComment'  # поле связанное с моделью Announcement и в форму попадут все объекты данной модели. Но нам нужны объекты ТОЛЬКО пренадлежащие текущему авторизованному пользователю, для этого переопределяем кверисет
        ]

    def __init__(self, *args, **kwargs):  # для этого переопределяем инициализатор в AnnouncementFilter
        super(AnnouncementFilter, self).__init__(*args, **kwargs)  # получаем конструктор родительского класса
        self.filters['adComment'].queryset = Announcement.objects.filter(responder__user_id=kwargs['request'])  # переопределяем кверисет объектов попадающих в наше поле
