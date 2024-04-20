import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")
clean_df = df.dropna()
min_sal_idx = clean_df["Starting Median Salary"].idxmin()
clean_df["Undergraduate Major"].loc[min_sal_idx]
clean_df["Starting Median Salary"].min()

idx_ = clean_df['Mid-Career Median Salary'].idxmin()
clean_df["Undergraduate Major"].loc[idx_]

spread_col = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
clean_df.insert(1, 'Spread', spread_col)
low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

th90 = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
th90[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

spread_col = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
#clean_df.insert(1, 'Spread', spread_col)
highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

pd.options.display.float_format = lambda x: '{:_.2f}'.format(x).replace('.', ',').replace('_', '.')
group_col = clean_df['Group']
no_string_data = clean_df.select_dtypes(include="number")
no_string_data.insert(1, 'Group', group_col)
no_string_data.groupby('Group').mean()
