from django import forms
from .models import VideoRequest

class VideoRequestForm(forms.ModelForm):
    color_choices = [
        ('#FFFFFF', 'Белый'),
        ('#FF0000', 'Синий'),
        ('#00FF00', 'Зеленый'),
        ('#0000FF', 'Красный'),
        ('#FFFF00', 'Голубой'),
        ('#FF00FF', 'Пурпурный'),
        ('#00FFFF', 'Желтый'),
    ]

    input_text = forms.CharField(max_length=255, label='Текст (не более 255 символов)')
    video_width = forms.IntegerField(min_value=100, max_value=500, initial=100, label='Ширина видео (от 100 до 500 пиксель')
    video_height = forms.IntegerField(min_value=100, max_value=500, initial=100, label='Высота видео (от 100 до 500 пиксель')
    duration = forms.IntegerField(min_value=3, max_value=60, initial=3, label='Продолжительность (от 3 до 60 секунд)')
    fontsize = forms.FloatField(min_value=1.0, max_value=4.0, initial=1.0, label='Высота текста (от 1 до 4)')
    color = forms.ChoiceField(choices=color_choices, label='Цвет текста')

    class Meta:
        model = VideoRequest
        fields = ['input_text', 'video_width', 'video_height', 'duration', 'fontsize', 'color']
