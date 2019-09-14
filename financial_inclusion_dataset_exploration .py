# Import Libraries
import pandas as pd

df = pd.read_csv('http://bit.ly/FinancialDataset')

df.head()

df.tail(10)

df.info()

df.describe()

df.shape

df.columns

df.year.unique()

df['Type of Job'].unique()

df['marital_status'].nunique()

df['Level of Educuation'].unique()

#viewing the unique values in the column

len(df['The relathip with head'].unique())

import matplotlib.pyplot as plt

import seaborn as sns
df.columns

df.dropna(inplace = True)

#plotting a histogram using matplotlib and seaborn

plt.figure(figsize = (12, 7))
sns.distplot(df['Respondent Age'], color= 'maroon')
plt.title('Distribution for Respodent Age')
plt.xlabel('Respodent')
plt.ylabel('Frequency')
plt.show()

df ['Respondent Age'].mean()

df ['Respondent Age'].skew()

plt.figure(figsize = (8, 5))
sns.countplot(df['country'])
plt.title('Country bar chart', color = 'red', fontdict={'size':18})
plt.show()

plt.figure(figsize = (8, 5))
sns.countplot(df['marital_status'])
plt.title('marital_status bar chart', color = 'red', fontdict={'size':18})
plt.show()

