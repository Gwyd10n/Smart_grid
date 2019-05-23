import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


data = pd.read_csv('TEST_District_1_random_n_times.csv')

distances = data[data.columns[1]]

sns.distplot(distances)

plt.show()
