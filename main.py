import pandas as pd
#from pandas_profiling.utils.common import extract_zip
from pandas_profiling import ProfileReport
#from pathlib import Path

### Energy per hour data
'''
dataset_name = 'energy_per_hour'
df = pd.read_csv('./data/%s.csv'% dataset_name,sep=';',header=0)

energy_report = ProfileReport(df)

print(energy_report.report.content)

# saving report to HTML file
html_file = open('./results/%s_profiling.html'% dataset_name,'w')
html_file.write(energy_report.html)
html_file.close()
'''

### Vehicles data
dataset_name = 'vehicles'
df = pd.read_csv('./data/%s.csv'% dataset_name,nrows=100)

vehicles_report = ProfileReport(df)

print(vehicles_report.report.content)

# saving report to HTML file
html_file = open('./results/%s_profiling.html'% dataset_name,'w')
html_file.write(vehicles_report.html)
html_file.close()

