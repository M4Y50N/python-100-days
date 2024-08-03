import pandas as pd
import matplotlib.pyplot as plt


df_tesla = pd.read_csv('data/TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-19.csv')

df_tesla.describe()

print(f'Largest value for Tesla in Web Search:', df_tesla.TSLA_WEB_SEARCH.max())
print(f'Smallest value for Tesla in Web Search:', df_tesla.TSLA_WEB_SEARCH.min())
















