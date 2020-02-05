# setup
import pandas as pd

df = pd.read_csv("csv/apple.csv", sep='\s*,\s*', header=0, encoding='ascii', engine='python')
X = df['Low'].values.reshape(-1,1)
y = df['High'].values.reshape(-1,1)
