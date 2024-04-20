import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("QueryResults.csv", names=['Date', 'TagName', 'Qtd'], header=0)

df.head()
df.tail()

df.shape
df.count()

df.groupby("TagName")["Qtd"].sum()
df.groupby("TagName")["Qtd"].count()

df.Date = pd.to_datetime(df["Date"])
df

df.shape

df.columns

df.head()

reshaped_df = df.pivot_table(index="Date", columns="TagName", values="Qtd")
reshaped_df

reshaped_df.fillna(0, inplace=True)
plt.figure(figsize=(20,12))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Date", fontsize=20)
plt.ylabel("Quantity", fontsize=20)
plt.plot(reshaped_df.index, reshaped_df["python"], linewidth=3, label=reshaped_df["python"].name)
plt.legend(loc="best", fontsize=18)

plt.figure(figsize=(20,12))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Date", fontsize=20)
plt.ylabel("Quantity", fontsize=20)
plt.plot(reshaped_df.index, reshaped_df["java"], linewidth=3, label=reshaped_df["java"].name)
plt.plot(reshaped_df.index, reshaped_df["python"], linewidth=3, label=reshaped_df["python"].name)
plt.legend(loc="best", fontsize=18)

roll_df = reshaped_df.rolling(window=12).mean()

plt.figure(figsize=(20,12))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Date", fontsize=20)
plt.ylabel("Quantity", fontsize=20)
plt.plot(roll_df.index, roll_df, linewidth=3, label=roll_df.columns)
plt.legend(loc="best", fontsize=18)
