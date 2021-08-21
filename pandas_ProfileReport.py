import pandas as pd
#from pandas_profiling.utils.common import extract_zip
from pandas_profiling import ProfileReport
#from pathlib import Path
import os.path

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

def Generate_Profile_Report(dataframe,html_file_name='profile_report.html',dst_path='./results/'):
    #Creating report
    report = ProfileReport(dataframe)
    # saving report to HTML file
    html_file = open('%s/%s'% (dst_path,html_file_name),'w')
    html_file.write(report.html)
    html_file.close()
    print('Report generated and saved in %s%s' % (dst_path,html_file_name))

### Vehicles data
dataset_name = 'vehicles'
df = pd.read_csv('./data/%s.csv'% dataset_name,nrows=100)
print('..data loaded')

if(not os.path.isfile('./results/vehicles_profiling.html')):
    Generate_Profile_Report(df,html_file_name='vehicles_profiling.html',dst_path='./results')
print('..profiling done')

print(df.head(9))
print(df.columns)

