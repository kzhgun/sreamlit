import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv('movehubqualityoflife.csv')
df.rename(columns={'lng':'lon'},inplace=True)

df['Pollution'] = 100 - df['Pollution']
df['Crime Rating'] = 100 - df['Crime Rating']


st.title('Best Cities to Live')

cols = df.columns

buttons = dict()
for i in range(1,7):
    buttons[i] = st.checkbox(cols[i])

criteria = []
for i in range(1,7):
    if buttons[i]:
        criteria.append(i)


df['score'] = 0

for elem in criteria:
    df['score'] += df.apply(lambda x: x[elem] / len(criteria), axis=1)



res = df.sort_values(by=['score'], ascending=False)
st.write(res.head(10))


st.map(res[['City','lat','lon']].iloc[:10])

