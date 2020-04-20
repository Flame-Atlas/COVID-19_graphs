import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('USA', 'Iran', 'Italy', 'Taiwan', 'India')
y_pos = np.arange(len(objects))
performance = [3154.384, 299.204, 1117.404, 49.748, 244.893]

plt.bar(y_pos, performance, align='center', color=['cyan'], alpha=0.5)
plt.xticks(y_pos, objects)
plt.xlabel('Country Names --- >')
plt.ylabel('Number of Tests (In Thousands)--->')
plt.title('Total Number of COVID-19 Tests(till April 15, 2020)')

plt.show()
