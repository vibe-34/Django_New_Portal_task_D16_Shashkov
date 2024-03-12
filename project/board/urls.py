from django.urls import path
from .views import AnnouncementList, AnnouncementDetail, AnnouncementCreate, AnnouncementUpdate, AnnouncementDelete, \
    UserResponseCreate

urlpatterns = [
    path('', AnnouncementList.as_view(), name='announcements'),
    path('create/', AnnouncementCreate.as_view(), name='announcement_create'),
    path('<int:pk>', AnnouncementDetail.as_view(), name='announcement_detail'),
    path('<int:pk>/update/', AnnouncementUpdate.as_view(), name='announcement_update'),
    path('<int:pk>/delete/', AnnouncementDelete.as_view(), name='announcement_delete'),
    path('<int:pk>/userresponse/create', UserResponseCreate.as_view(), name='userresponse_create'),
]
