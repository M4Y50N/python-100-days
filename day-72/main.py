import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")
clean_df = df.dropna()

print(clean_df.head())

print(clean_df.tail())

print(clean_df.shape)
print(clean_df.columns)
print(clean_df[['Undergraduate Major', 'Starting Median Salary',
       'Mid-Career Median Salary', 'Mid-Career 10th Percentile Salary']].head())
print(clean_df[clean_df['Undergraduate Major'] == 'Computer Science'])

pd.options.display.float_format = lambda x: '{:_.2f}'.format(x).replace('.', ',')
only_numbers = clean_df.select_dtypes(include="number")
group_col = clean_df['Group']
only_numbers.insert(1, 'Group', group_col)

print(only_numbers.groupby('Group').mean())
