from django.db import models

class VideoRequest(models.Model):
    input_text = models.CharField('Текст', max_length=255, default='Текст')
    video_width = models.IntegerField('Высота', max_length=500, default=100)
    video_height = models.IntegerField('Ширина', max_length=500, default=100)
    duration = models.IntegerField('Продолжительность', max_length=60, default=3)
    fontsize = models.FloatField()
    color = models.CharField(max_length=7)  # Формат цвета в виде HEX, например, #FFFFFF
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.input_text} - {self.created_at}"

    class Meta:
        verbose_name = 'Бегущая строка'
        verbose_name_plural = 'Бегущие строки'