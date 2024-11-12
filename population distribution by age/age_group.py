from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('india_population_by_age_groups.csv')

plt.figure(figsize=(10,6))
plt.bar(data['Age Group'], data['Population'], color='skyblue', edgecolor='black')

y_ticks = [i * 100000000 for i in range(1, 10)] 
plt.yticks=(y_ticks)

plt.title('Population of India per age group')
plt.xlabel('Age groups')
plt.ylabel('Population')

plt.tight_layout()

plt.show()
