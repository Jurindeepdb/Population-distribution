from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('male_population.csv')

plt.figure(figsize=(10,6))
plt.plot(data['Year'], data['Percentage'], marker='o', linestyle='-', color='blue', label='Percentage')
  
y_ticks = [i * 0.5 for i in range(102, 105)] 
plt.yticks=(y_ticks)

plt.title('Percentage of males in the Indian population')
plt.xlabel('Year')
plt.ylabel('Percentage')

plt.ylim(51, 52.0)
plt.tight_layout()

plt.show()
