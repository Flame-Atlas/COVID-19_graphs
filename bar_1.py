import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('USA', 'Iran', 'Italy', 'China', 'Taiwan', 'India')
y_pos = np.arange(len(objects))
performance = [6224.12, 736.89, 1651.55, 821.60, 3.95, 123.20]

plt.bar(y_pos, performance, align='center', color=['blue'], alpha=0.5)
plt.xticks(y_pos, objects)
plt.xlabel('Country Names --- >')
plt.ylabel('Number of Cases (In Hundreds)--->')
plt.title('Total Number of COVID-19 cases(till April 15, 2020)')

plt.show()
