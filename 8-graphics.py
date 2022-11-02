from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker

with open("settings.txt", "r") as file:
    settings = [float(i) for i in file.read().split("\n")]
#считываем показания компаратора и переводим через шаг квантования в вольиты
data=numpy.loadtxt('data.txt', dtype=int) * settings[1]
#массив времен, создаваемый черед количество измерений и известный шаг по времени
data_time=numpy.array([i*settings[0] for i in range(data.size)])
#параметры фигуры
fig, ax=pyplot.subplots(figsize=(16, 10), dpi=500)

#минимальные и максимальные значения для осей
ax.axis([0, data_time.max()+1, 0, data.max()+0.2])

#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

#название графика с условием для переноса строки и центрированием
ax.set_title("\n".join(wrap('Процесс заряда и разряда конденсатора в RC цепи', 60)), loc = 'center')

#сетка основная и второстепенная
ax.grid(which='major', color = 'gray')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

#подпись осей
ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, с")

#линия с легендой
ax.plot(data_time, data, c='blue', linewidth=1, label = 'V(t)')
#Маркеры
ax.scatter(data_time[0:data.size:200], data[0:data.size:200], marker = 's', c = 'red', s=200)

ax.legend(shadow = False, loc = 'upper right', fontsize = 30)

#Добавление текста  https://pyprog.pro/mpl/mpl_text.html 
ax.text(32, 2.5, 'Время зарядки = 26.3 с', rotation = 0, fontsize = 30)
ax.text(32, 2, 'Время разрядки = 33.7 с', rotation = 0, fontsize = 30)

#сохранение
fig.savefig('graph.png')
fig.savefig('graph.svg')
