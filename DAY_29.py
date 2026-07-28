'''
=> MATPLOTLIB
- matplotlib library is a python library that provides functionality to charts, graphs, bar graphs and data visulization

import matplotlib.pyplot as plt
x = [10,20,30,40,50]
y = [100,150,200,250,300]
plt.plot(x,y)
plt.title("car sales")
plt.xlabel("year")
plt.ylabel("sales")
plt.show()


- LINE PLOT:-

import matplotlib.pyplot as plt
x = [2005,2010,2015,2020,2025]
y = [600,150,221,540,350]
plt.plot(x,y)
plt.title("CAR SALES")
plt.xlabel("year")
plt.ylabel("sales")
plt.show()


- BAR PLOT:-

import matplotlib.pyplot as plt
x = [2005,2010,2015,2020,2025]
y = [600,150,221,540,350]
plt.bar(x,y,color='aquamarine', edgecolor='black', width=3 )
plt.title("CAR SALES")
plt.xlabel("year")
plt.ylabel("sales")
plt.show()

- PIE CHART

import matplotlib.pyplot as plt
x = ['groceries','shopping','food','fees','rent']
y = [17,9,23,40,30]
plt.pie(y,labels=x,colors=['aquamarine','pink','lightblue','cyan','plum'],autopct='%1.1f%%')
plt.legend(x)
plt.title("EXPENDITURE")
plt.show()

- SCATTER PLOT

import matplotlib.pyplot as plt
x = [2005,2010,2015,2020,2025]
y = [600,150,221,540,350]
plt.scatter(x,y,color='aquamarine')
plt.title("CAR SALES")
plt.xlabel("year")
plt.ylabel("sales")
plt.show()

- HISTOGRAM

import matplotlib.pyplot as plt
y = [10,20,30,40,50]
plt.hist(y,bins=20)
plt.title('neku yeduku')
plt.xlabel('avasarama')
plt.ylabel('sarle')
plt.show()

'''
import matplotlib.pyplot as plt
x = ['groceries','shopping','food','fees','rent']
y = [17,9,23,40,30]
plt.title("expenditure")
x_lab = "expenses"
y_lab = "amount used"
plt.figure(figsize=(6,8))
plt.subplot(2,2,1)
plt.plot(x,y)

plt.xlabel(x_lab)
plt.ylabel(y_lab)

plt.subplot(2,2,2)
plt.bar(x,y,color='aqua', edgecolor='black')
plt.title(title)
plt.xlabel(x_lab)
plt.ylabel(y_lab)

plt.subplot(2,2,3)
plt.scatter(x,y,color='aquamarine')

plt.xlabel(x_lab)
plt.ylabel(y_lab)

plt.subplot(2,2,4)
plt.pie(y,labels=x,colors=['aquamarine','pink','lightblue','cyan','plum'],autopct='%1.1f%%')
plt.xlabel(x_lab)
plt.ylabel(y_lab)

plt.legend(x)

plt.xlabel(x_lab)
plt.ylabel(y_lab)
plt.show()





















