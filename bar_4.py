import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('USA', 'Iran', 'Italy', 'China', 'Taiwan', 'India')
y_pos = np.arange(len(objects))
performance = [5471.16, 216.79, 1054.18, 11.37, 2.52, 104.83]
plt.bar(y_pos, performance, align='center', color=['orange'], alpha=0.5)
plt.xticks(y_pos, objects)
plt.xlabel('Country Names --- >')
plt.ylabel('Number of Active Cases (In Hundreds)--->')
plt.title('Active Cases of COVID-19 Active cases(till April 15, 2020)')

plt.show()
