import pandas as pd
import random
import matplotlib.pyplot as plt


df = pd.DataFrame([random.randint(1,100) for _ in range(200)],index=range(200),columns=['sales'])
print(df.head())
