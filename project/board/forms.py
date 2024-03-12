from django import forms
from django.core.exceptions import ValidationError

from .models import Announcement, UserResponse


class AnnouncementForm(forms.ModelForm):
    text = forms.CharField(min_length=16,)

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if title[0].isLower():
    #         raise ValidationError('Заголовок должен быть с заглавной буквы')
    #     return title
    #
    # def clean_text(self):
    #     title = self.cleaned_data['title']
    #     if title[0].isLower():
    #         raise ValidationError('Описание должно быть с заглавной буквы')
    #     return title

    class Meta:
        model = Announcement
        fields = ['author', 'title', 'text', 'category', 'upload', ]


class UserResponseForm(forms.ModelForm):  # класс формы отклика
    class Meta:
        model = UserResponse
        fields = ['text']
        labels = {'text': 'Введите текст отклика'}
        widgets = {'text': forms.Textarea(attrs={'class': 'form-text', 'cols': 200, 'rows': 2})}


