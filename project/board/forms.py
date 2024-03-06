from django import forms
from django.core.exceptions import ValidationError

from .models import Announcement


class AnnouncementForm(forms.ModelForm):
    text = forms.CharField(
        min_length=8,
    )

    class Meta:
        model = Announcement
        fields = ['author', 'title', 'text', 'category', 'upload', ]


