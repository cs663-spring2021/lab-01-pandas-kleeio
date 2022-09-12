
import pandas as pd
import numpy as np
import matplotlib


FILE = "property_permits.csv"
df = pd.read_csv("property_permits.csv", low_memory=False)
print(df.head())
