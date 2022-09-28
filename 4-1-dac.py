import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]
list = []
a = 3.3 

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac,GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def ifnumber(a):
    try:
        num = int(a)
    else:
        return num
    except Exception:
        print("Вы ввели не число!")
        return 0
    finally:
        

def work():
    try:
        while True: 
            word = input()
            if word == 'q':
                GPIO.output(dac,0) 
                GPIO.cleanup()
                break
            number = ifnumber(word)
            list = decimal2binary(number)
            GPIO.output(dac, list)
            v = 0
            for i in range (0, len(list)):
                if list[i] == 1:
                    v += a/8
            v = round(v, 2)
            print("Предполагаемое напряжение на выходе:", v, "В")
    finally: 
        GPIO.output(dac,0) 
        GPIO.cleanup() 

work()       
