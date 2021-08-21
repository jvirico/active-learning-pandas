import pandas as pd
import numpy as np

# Series
series = pd.Series([1,2,3])
series.name = 'numbers'
print(series)

# DataFrames
df = pd.DataFrame({'col1':['a','b','c'], 'col2':series})
print(df)
print(df.shape)

df = pd.read_csv('./data/iris.data', header=None)
print(df.head(6))
print(df.tail(6))

col_names = ['sepalo_len','sepalo_width', 'petalo_len','petalo_width','class']
df.columns = col_names
print(df.head(6))

print(df.index)
print(df.columns)
print(df.describe())
print('')
print(df['class'].value_counts())
print(df.T)
print(df.sort_values('sepalo_width',ascending=True))
print('')
print(df[['class','sepalo_len']])
## Filtering
# filter rows [4,10,100] and cols [4,0]
print(df.iloc[[3,6,9],[4,0]])
print(df[df['sepalo_len']> 5])
print(df[df['sepalo_len']> 5].size)

## finding NaNs
print(df.isna().sum().sum())
## lets indroduce some NaNs
df['sepalo_len'][:10] = np.nan
print(df.head(20))
