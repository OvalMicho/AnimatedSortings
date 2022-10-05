import RPi.GPIO as GPIO
import time

leds = [21,20,16,12,7,8,25,24]
dac = [26,19,13,6,5,11,9,10]
comp = 4
troyka = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)

a=int()

def func(a):
    return[int(i) for i in bin(a)[2:].zfill(8)]

def adc():
    count = 0
    for i in range (7, -1, -1):
        signal = func((count + 2**i))
        GPIO.output(dac,signal)
        time.sleep(0.001)
        compvalue = GPIO.input(comp)
        if compvalue == 1:
            count += 2**i
    return count

def volum(voltage):
    v = float(3.3 / 8)
    v_v = v
    list = [0,0,0,0,0,0,0,0]
    for i in range (7, -1, -1):
        if voltage > v_v:
            list[i] = 1
            v_v += v
    GPIO.output(leds, list)


try:
    while True:
        k=adc()
        voltage= float(int(3.3*k/256*100)/100)
        volum(voltage)
        print("ADC value= ",k," -> ",func(k),"voltage= ",voltage)
    
finally:
    GPIO.output(dac,1)
    GPIO.cleanup()