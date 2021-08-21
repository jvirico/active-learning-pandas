import pandas as pd
import numpy as np
import data_prep_utils as dprep


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

df_ori = df.copy()
dprep.RunNormalityAnalysis(df_ori['sepalo_len'])

## finding NaNs
print(df.isna().sum().sum())
## lets indroduce some NaNs
df['sepalo_len'][:10] = np.nan
print(df.head(20))
print(df.isna().sum())
print(df['sepalo_len'].mean())
print(df['sepalo_len'].median())
df['sepalo_len'] = df['sepalo_len'].fillna(df['sepalo_len'].median())
print(df.head(20))

df = df.assign(sepalo_ratio = lambda x:x['sepalo_len']/x['sepalo_width'])
df = df.assign(petalo_ratio = lambda x:x['petalo_len']/x['petalo_width'])
print(df.head(9))

# DataFrame column normalization
def normalize(df,columns):
    result = df.copy()
    for feature_name in columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

df_normalized = normalize(df,['sepalo_ratio','petalo_ratio'])
print(df_normalized.head(9))

#dprep.RunNormalityAnalysis(df_normalized['sepalo_ratio'])