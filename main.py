#
#
#

import pandas as pd

### READING THE WHOLE FILE ###

df_csv = pd.read_csv('pokemon.csv')
# print(df.head(3))
# print(df.tail(3))

df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(3))

df = pd.read_csv('pokemon.txt', '\t')
# print(df.head(5))

### READING COLUMNS ###

# print(df.columns)  # Tells you what kinds of columns you have
# print(df['Name'])
# print(df['Name'][:10])
# print(df[['Name', 'Type 1', 'Type 2']][:13])

### READING ROWS ###

# print(df.iloc[0])  # "iloc" stands for integer location
# print()
# print(df.iloc[0:3])
# print()
# print(df.iloc[2,1].upper())

# print(df.loc[df['Type 1'] == 'Fairy'])  # "loc" is just location

# ITERATING THROUGH ROWS #

# for index, row in df.iterrows():
#    print(index, row)

# for i, r in df.iterrows():
#    print(i, r['Name'])

### DESCRIBING DATA ###

# print(df.describe())  # Gives data on the mean and standard devs etc

### SORTING DATA ###

# print(df.sort_values('Name'))
# print(df.sort_values('Name', ascending=False))

# print(df.sort_values(['Type 1', 'HP']))  # Type is alphabetical, HP is ascending
# print(df.sort_values(['Type 1', 'HP'], ascending=False))
# print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))  # I think 1 means True and 0 means False
# print(df.sort_values(['Type 1', 'HP'], ascending=[0,1]))

### CHANGING DATA ###



