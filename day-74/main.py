import pandas as pd
import matplotlib.pyplot as plt

colors = pd.read_csv('data/colors.csv')
colors['name'].nunique()

colors.is_trans.value_counts()
colors.groupby('is_trans').count()

sets = pd.read_csv('data/sets.csv')
sets.head()
sets.tail()

sets.sort_values('year').head()

# Set per years
sets[sets['year'] == 1949]

# Lego with most number of parts
sets.sort_values('num_parts', ascending=False).head()

# Set num per year
sets_by_year = sets.groupby('year').count()
sets_by_year['set_num'].head()

# Graphic view
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])

# Themes per year
themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
themes_by_year.head()

# Graphic view
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])

# 2 graphs at same time
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])

# Separated axes
# Line Charts with Two Separate Axes
ax1 = plt.gca()  # creating axis
ax2 = ax1.twinx()  # create another axis that shares the same x-axis

# Add styling
ax1.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='g')
ax2.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], 'b')

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='green')
ax2.set_ylabel('Number of Themes', color='blue')

# Average num of parts per set
parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
# Scatter graph
plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2], s=17, c='#ff7f0e')

# Count set parts per theme
set_theme_count = sets['theme_id'].value_counts()
set_theme_count.head()

# Themes CSV
themes = pd.read_csv("data/themes.csv")

# Get Start Wars themes
star_wars_themes = themes[themes.name == 'Star Wars']

# Creating a data frame with theme_id and set_count
set_theme_count = pd.DataFrame({'id': set_theme_count.index, 'set_count': set_theme_count.values})
set_theme_count.head()

# Merging 2 data frames
merged_df = pd.merge(set_theme_count, themes)
merged_df.head()

# Graphic View
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])