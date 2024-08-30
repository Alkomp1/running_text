import cv2
import numpy as np

def create_running_text_video(text, video_width=100, video_height=100, duration=3, fps=24, fontsize=1, color=(255, 255, 255), output_file='running_text.avi'):
    # Вычисляем количество кадров
    num_frames = duration * fps

    # Создаем видео
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(output_file, fourcc, fps, (video_width, video_height))

    for i in range(num_frames):
        # Создаем пустой кадр
        frame = np.zeros((video_width, video_height, 3), dtype=np.uint8)

        # Вычисляем позицию текста
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, fontsize, 1)[0]
        text_width = text_size[0]
        text_height = text_size[1]
        x_position = video_width - int(i * (text_width + video_width) / num_frames)
        y_position = (video_height + text_height) // 2

        # Наносим текст на кадр
        cv2.putText(frame, text, (x_position, y_position), cv2.FONT_HERSHEY_SIMPLEX, fontsize, color, 1, cv2.LINE_AA)

        # Добавляем кадр в видео
        video.write(frame)

    # Завершаем создание видео
    video.release()

# Пример использования функции
create_running_text_video("день", video_width=100, video_height=100, duration=3, fontsize=1, color=(255, 255, 255), output_file='running_text.avi')