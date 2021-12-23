import pandas as pd

# Series - 1D Collection
# Data Frame - 2D Collection
df = pd.read_csv('players.csv')
# print(df)
# print(df['First name'])
print(df.iloc[0])

