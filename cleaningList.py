import pandas as pd

jobListDF = pd.read_csv(r'/Users/chairman/JobsAnacPyCharm/bestjoblist1.csv').fillna(0)
jobListDF.drop('Unnamed: 0', axis='columns', inplace=True)
jobListDF.columns = ['Organisation Name', 'Location', 'Tier Rating']



groupedListDF = jobListDF.groupby(['Organisation Name', 'Location'], as_index=False, sort=False)['Tier Rating'].apply(', '.join)

groupedListDF.to_csv('finalJobList.csv')

