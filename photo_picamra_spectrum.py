from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.brightness = 53

camera.start_preview() # Camera warm-up time - Отображение входных данных камеры в ральном времени

brightness = str(camera.brightness)
resolution = str(camera.resolution)
contrast = str(camera.contrast)
print('Яркость камеры: ' + brightness + '%')
print('Разрешение снимков камеры: ' + resolution + 'пикселей')
print('Контрастность снимков камеры: ' + contrast + 'едениц')

sleep(2)
camera.capture('mercury_white.png') # Take a picture - и сохранение фото

#camera.stop_preview() - остановка предварительного просмотра

#camera.resolution = (1280, 720) - задание разрешения снимка
#camera.contrast = 10 - задание контраста снимка

#camera.close() -   метод для освобождения ресурсов камеры