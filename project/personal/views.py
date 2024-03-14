from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from board.models import UserResponse
from personal.filters import AnnouncementFilter


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'personal/index.html'

# определяем контекст для фильтра = переопределяем метод get_context_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # берем контекст из родительского класса и передаем в него аргументы
        # определяем кверисет отзывов, которые принадлежат объявляниям текущего авторизованного пользователя
        queryset = UserResponse.objects.filter(adComment__author__user_id=self.request.user.id)
        # определяем контекстную переменную
        context['filterset'] = AnnouncementFilter(self.request.GET, queryset, request=self.request.user.id)
        # возвращаем наш контекст
        return context
