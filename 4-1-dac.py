import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]
list = []
a = 3.3 

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac,GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def work():
    try:
        while True: 
            word = input()
            if word == 'q':
                break
            if word.isdigit() and int(word)<=255:
                number = int(word)
                list = decimal2binary(number)
                GPIO.output(dac, list)
                v = number / 256 * 3.3
                v = round(v, 2)
                print("Предполагаемое напряжение на выходе:", v, "В")
            else:
                print("Вы ввели число не того формата, введите положительное целое число от 0 до 255:")
    finally: 
        GPIO.output(dac,0) 
        GPIO.cleanup() 

work()       
