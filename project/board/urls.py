from django.urls import path
from .views import AnnouncementList, AnnouncementDetail, AnnouncementCreate, AnnouncementUpdate, AnnouncementDelete

urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', AnnouncementList.as_view(), name='announcements'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', AnnouncementDetail.as_view(), name='announcement_detail'),
    path('create/', AnnouncementCreate.as_view(), name='announcement_create'),
    path('<int:pk>/update/', AnnouncementUpdate.as_view(), name='announcement_update'),
    path('<int:pk>/delete/', AnnouncementDelete.as_view(), name='announcement_delete'),
]
