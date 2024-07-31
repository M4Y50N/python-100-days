import pandas as pd
import matplotlib.pyplot as plt

colors = pd.read_csv('data/colors.csv')
print(colors['name'].nunique())
