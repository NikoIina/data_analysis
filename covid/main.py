import pandas as pd
from matplotlib import pyplot as plt

cases = pd.read_csv('covid_cases_de.csv')
# hospitals = pd.read_excel('covid_hospitals.xlsx')
testing = pd.read_excel('covid_testing.xlsx')
worldwide = pd.read_excel('covid_worldwide.xlsx')

# print(testing[0:10])
russia_cases = (worldwide['country'] == 'Germany') & (worldwide['indicator'] == 'cases')
dates = []
n_cases = []
all_russia_casses = worldwide.loc[russia_cases, ['weekly_count', 'year_week']]
for index, row in all_russia_casses.iterrows():
    dates.append(row['year_week'])
    n_cases.append(row['weekly_count'])

plt.plot(dates,n_cases)
plt.show()