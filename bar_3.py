import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('USA', 'Iran', 'Italy', 'China', 'Taiwan', 'India')
y_pos = np.arange(len(objects))
performance = [477.07, 499.93, 380.92, 778.16, 137.0, 143.12]
plt.bar(y_pos, performance, align='center', color=['green'], alpha=0.5)
plt.xticks(y_pos, objects)
plt.xlabel('Country Names --- >')
plt.ylabel('Number of Recovered Cases (In Hundreds)--->')
plt.title('Total Number of COVID-19 Recovered cases(till April 15, 2020)')

plt.show()

