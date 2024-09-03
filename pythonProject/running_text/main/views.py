from django.shortcuts import render, redirect
from .forms import VideoRequestForm
from .models import VideoRequest
import cv2
import numpy as np
from django.http import HttpResponse
from django.conf import settings
import os

def index(request):
    data = {
        'title': 'Главная страница'
    }
    return  render(request, 'main/index.html', data)

def create_running_text_video(text, video_width=100, video_height=100, duration=3, fps=24, fontsize=1, color=(255, 255, 255), output_file='running_text.avi'):
    num_frames = duration * fps
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(output_file, fourcc, fps, (video_width, video_height))
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_COMPLEX, fontsize, 1)[0]
    text_width = text_size[0]
    text_height = text_size[1]

    for i in range(num_frames):
        frame = np.zeros((video_height, video_width, 3), dtype=np.uint8)
        x_position = video_width - int(i * (text_width + video_width) / num_frames)
        y_position = (video_height + text_height) // 2
        cv2.putText(frame, text, (x_position, y_position), cv2.FONT_HERSHEY_COMPLEX, fontsize, color, 1, cv2.LINE_AA)
        video.write(frame)
    video.release()

def video_request_view(request):
    if request.method == 'POST':
        form = VideoRequestForm(request.POST)
        if form.is_valid():
            video_request = form.save()

            # Конвертируем HEX цвет в формат BGR для OpenCV
            color_hex = video_request.color.lstrip('#')
            color_rgb = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))

            # Указываем путь для сохранения видео
            output_file = 'running_text.avi'
            output_path = os.path.join(settings.MEDIA_ROOT, 'videos', output_file)

            # Создаем видео
            create_running_text_video(
                text=video_request.input_text,
                video_width=video_request.video_width,
                video_height=video_request.video_height,
                duration=video_request.duration,
                fontsize=video_request.fontsize,
                color=color_rgb,
                output_file=output_path
            )

            # Открываем файл и отправляем его пользователю
            with open(output_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='video/x-msvideo')
                response['Content-Disposition'] = f'attachment; filename="{output_file}"'
                return response

    else:
        form = VideoRequestForm()

    return render(request, 'main/running_text.html', {'form': form})