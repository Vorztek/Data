import pandas as pd
from IPython.display import display
from IPython.core.interactiveshell import InteractiveShell
import matplotlib.pyplot as plt

with open(r'C:\Users\vion1\Ele\Engie\Exercices\ML\Manga\top_1000.csv', encoding="utf8") as file:
    df = pd.read_csv(file)


pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)
pd.set_option('precision', 0)

print(df[["Title", "Rank"]])