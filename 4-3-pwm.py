import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)

try:
    p = GPIO.PWM(18, 1000)
    p.start(0)
    while True:
        duty = int(input("Введите значение duty cycle в %:"))
        p.ChangeDutyCycle(duty)
    p.stop()
finally:
    GPIO.output(5,0)
    GPIO.cleanup()

#https://www.electronicwings.com/raspberry-pi/raspberry-pi-pwm-generation-using-python-and-c 