import pandas as pd
from io import StringIO
str_data = r"""
date,weather
2018-03-04, cloudy
2018-03-05, sunny
2018-03-06, rain
"""

df = pd.read_csv(StringIO(str_data))
print(df)
df['Is cloudy'] = df['weather'].apply(lambda x: 'Y' if 'cloudy' in x else 'N')
df['Is sunny'] = df['weather'].apply(lambda x: 'Y' if 'sunny' in x else 'N')
mask=df['weather'].str.contains('r',na=False)
print(df)
print(df[mask])