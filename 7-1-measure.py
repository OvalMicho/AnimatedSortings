import RPi.GPIO as GPIO
import time
import matplotlib
from matplotlib import pyplot as plt
GPIO.setwarnings(False)

leds=[21,20,16,12,7,8,25,24]
dac = [26,19,13,6,5,11,9,10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds,GPIO.OUT)
GPIO.output(leds,0)
GPIO.setup(dac,GPIO.OUT)
GPIO.output(dac,0)
GPIO.setup(comp,GPIO.IN)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
T0=time.time()

a=int()

def func(a):
    return[int(i) for i in bin(a)[2:].zfill(8)]

def adc():
    count = 0
    for i in range (7, -1, -1):
        signal = func((count + 2**i))
        GPIO.output(dac,signal)
        time.sleep(0.01)
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
    t=[]
    V=[]
    voltage=0
    tim= open("time.txt","at")
    #with open('time.txt','at') as tim0:
    #        tim0.write("0")
    #with open('volt.txt','at') as vol0:
    #        vol0.write("0") 

    while (voltage<3.3*(1-0.08)):
        k=adc()
        voltage= float(int(3.3*k/256*100)/100)
        volum(voltage)
        t.append(time.time()-T0)
        V.append(voltage)
        print("ADC value = ",k," -> ",func(k),"voltage = ",voltage)

        tim= open("time.txt","at")
        tim.write(str(time.time()-T0)+'\n');
        tim.close

        vol= open("volt.txt","at")
        vol.write(str(voltage)+'\n');
        vol.close
    
    Traz=time.time()-T0
    GPIO.setup(troyka,GPIO.OUT,initial=GPIO.LOW)    
    while (voltage>0.09):
        k=adc()
        voltage= float(int(3.3*k/256*100)/100)
        volum(voltage)
        t.append(time.time()-T0)
        V.append(voltage)
        print("ADC value = ",k," -> ",func(k),"voltage = ",voltage)  

        tim= open("time.txt","at")
        tim.write(str(time.time()-T0)+'\n');
        tim.close

        vol= open("volt.txt","at")
        vol.write(str(voltage)+'\n');
        vol.close  
    print("Длина массива ",len(t))
    print("Время ",t[len(t)-1], "c")
    print("Период 1-ого измерения:", t[len(t)-1]/len(t), "c")
    print("Частота ", len(t)/(t[len(t)-1]), "Гц")
    print("Шаг квантования ", 3.3/256)
    plt.plot(t,V)
    plt.xlabel("t,Сек")
    plt.ylabel("V,Вольт")
    plt.show()


finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
