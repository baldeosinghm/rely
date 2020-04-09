import pandas as pd
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TKagg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv("csv/apple.csv", sep='\s*,\s*', header=0, encoding='ascii', engine='python')
X = df['Low'].values.reshape(-1,1)
y = df['High'].values.reshape(-1,1)
