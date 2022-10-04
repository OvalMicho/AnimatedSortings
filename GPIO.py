import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)#Режим обращения к пинам

GPIO.setup(15, GPIO.OUT)#Настройка пина на выход
GPIO.setup(14, GPIO.IN)#Настройка пина на вход

while True: #Постоянное обновление статуса схемы платы
    if GPIO.input(14) == 1: #Входное значение на пин Y (от вольтажа 1/0)
        GPIO.output(15, 1)
    else:
        GPIO.output(15, 0)