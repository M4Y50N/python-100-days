import pandas as pd
import matplotlib.pyplot as plt


df_tesla = pd.read_csv('data/TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-19.csv')

df_tesla.describe()

print(f'Largest value for Tesla in Web Search:', df_tesla.TSLA_WEB_SEARCH.max())
print(f'Smallest value for Tesla in Web Search:', df_tesla.TSLA_WEB_SEARCH.min())

print('Largest value for "Unemployemnt Benefits" '
      f'in Web Search: {df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}')

df_btc_price.head()
df_btc_search.head()

print(f'largest BTC News Search: {df_btc_search.BTC_NEWS_SEARCH.max()}')

print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')
print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}')

print(f'Missing values for BTC price?: {df_btc_price.isna().values.any()}')
print(f'Number of missing values: {df_btc_price.isna().values.sum()}')

df_clean_btc_price = df_btc_price.dropna()

df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
type(df_tesla.MONTH[0])

df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
type(df_unemployment.MONTH[0])

df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)

print(type(df_btc_search.MONTH[0]))
print(type(df_btc_price.DATE[0]))

df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
# df_btc_monthly

df_btc_monthly2 = df_btc_price.resample('M', on='DATE').mean()
# df_btc_monthly



