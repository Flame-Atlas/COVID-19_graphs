import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('USA', 'Iran', 'Italy', 'China', 'Taiwan', 'India')
y_pos = np.arange(len(objects))
performance = [275.49, 47.77, 216.45, 33.41, 0.06, 4.05]
plt.bar(y_pos, performance, align='center', color=['red'], alpha=0.5)
plt.xticks(y_pos, objects)
plt.xlabel('Country Names --- >')
plt.ylabel('Number of Deaths (In Hundreds)  --->')
plt.title('Total Number of Deaths(till April 15, 2020)')

plt.show()

