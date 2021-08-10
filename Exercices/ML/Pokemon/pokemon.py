import pandas as pd
import csv
from IPython.display import display
from IPython.core.interactiveshell import InteractiveShell
import matplotlib.pyplot as plt
import seaborn as sns


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('precision', 0)

with open(r'C:\Users\vion1\Ele\Engie\Exercices\ML\Pokemon\pokemon.csv', encoding="utf8") as file:
    df = pd.read_csv(file)

#print(display(df.iloc[range(1,150)][['capture_rate',"name"]]))

#print(df.describe())
#print(df.corr())

plt.figure(figsize=(20, 10))
sns.heatmap(df.corr())