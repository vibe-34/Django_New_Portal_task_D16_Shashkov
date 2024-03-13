from datetime import datetime
from pprint import pprint

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

# Импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import AnnouncementFilter
from .forms import AnnouncementForm, UserResponseForm
from .models import Announcement, UserResponse


class AnnouncementList(ListView):
    model = Announcement  # Указываем модель, объекты которой мы будем выводить
    ordering = 'category'  # Поле, которое будет использоваться для сортировки объектов
    template_name = 'board/announcements.html'  # Указываем имя шаблона, в котором будут все инструкции о том, как именно пользователю должны быть показаны наши объекты
    context_object_name = 'announcements'  # Это имя списка, в котором будут лежать все объекты. # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    paginate_by = 3  # вот так мы можем указать количество записей на странице

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        queryset = super().get_queryset()  # Получаем обычный запрос
        # Используем наш класс фильтрации. self.request.GET содержит объект QueryDict, который мы рассматривали в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса, чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = AnnouncementFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        # context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class UserResponseCreate(LoginRequiredMixin, CreateView):
    model = UserResponse
    template_name = 'board/id_announcement.html'
    form_class = UserResponseForm

    def form_valid(self, form):
        userresponse = form.save(commit=False)
        userresponse.responder = self.request.user  # автором отклика будет текущий авторизованный пользователь
        userresponse.adComment_id = self.kwargs['pk']  # назначаем текущего пользователя, автором отклика
        userresponse.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcement_id'] = self.kwargs['pk']  # ссылаемся на идентификатор объявления к которому делаем отклик
        return context


class AnnouncementDetail(UserResponseCreate, DetailView):
    model = Announcement  # Модель всё та же, но мы хотим получать информацию по отдельному отзыву
    template_name = 'board/id_announcement.html'  # Используем другой шаблон — id_announcement.html
    context_object_name = 'id_announcement'  # Название объекта, в котором будет выбранный пользователем отзыв


class AnnouncementCreate(LoginRequiredMixin, CreateView):  # Представление для создания объявления.
    raise_exception = True  # Для выдачи ошибки с 403 кодом, для не авторизированных пользователей
    form_class = AnnouncementForm  # Указываем нашу разработанную форму
    model = Announcement  # модель объявления
    template_name = 'board/create.html'  # шаблон, в котором используется форма.
    success_url = reverse_lazy('announcements')  # указываем место, куда перенаправить пользователя после удаления

    def form_valid(self, form):
        announcement = form.save(commit=False)
        if self.request.method == 'POST':
            announcement.author = self.request.user
        announcement.save()
        return super().form_valid(form)



class AnnouncementUpdate(LoginRequiredMixin, UpdateView):  # Представление для редактирования объявления.
    raise_exception = True  # Для выдачи ошибки с 403 кодом, для не авторизированных пользователей
    form_class = AnnouncementForm
    model = Announcement
    template_name = 'board/update.html'
    success_url = reverse_lazy('announcements')  # указываем место, куда перенаправить пользователя после удаления


class AnnouncementDelete(LoginRequiredMixin, DeleteView):  # Представление удаляющее объявление.
    raise_exception = True  # Для выдачи ошибки с 403 кодом, для не авторизированных пользователей
    model = Announcement
    template_name = 'board/delete.html'
    success_url = reverse_lazy('announcements')  # указываем место, куда перенаправить пользователя после удаления
