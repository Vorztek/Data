import pandas as pd
import csv
from IPython.display import display
from IPython.core.interactiveshell import InteractiveShell
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('precision', 0)



with open(r'C:\Users\vion1\Ele\Engie\Exercices\ML\Pokemon\pokemon.csv', encoding="utf8") as file:
    df = pd.read_csv(file)

df.select_dtypes(include=['int64','float64']).columns
df.columns = df.columns.str.upper()
df['TYPE1'] = df['TYPE1'].str.capitalize()
df['TYPE2'] = df['TYPE2'].str.capitalize()
df['TYPE2'].fillna(value='None', inplace=True)
#print(display(df.iloc[range(1,150)][['capture_rate',"name"]]))

#print(df.describe())
#print(df.corr())

plt.figure(figsize=(15, 15))
#sns.heatmap(df.corr(), cmap = sns.color_palette("RdBu_r", 14))

sns.heatmap(
    df[df['TYPE2']!='None'].groupby(['TYPE1', 'TYPE2']).size().unstack(),
    linewidths=1,
    annot=True, cmap=sns.color_palette("RdBu_r", 7)
)

