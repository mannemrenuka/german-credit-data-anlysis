import pandas as pd
import matplotlib.pyplot as plt

def stats(num_cols, data):
    for column in num_cols[:-1]:
        print(column)
        print(data.groupby('classification')[column].describe())
        print('\n')
def plot_hue(li, hue, data):
    for col in li:
        data.groupby(hue)[col].plot(kind = 'hist', alpha = 0.5, legend = ['0','1'])
        plt.title(col)
        plt.show()
