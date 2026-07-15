import pandas as pd
import random 

df = pd.DataFrame([random.randint(1,10) for _ in range(10)],index=range(10),columns=['Forecast'])
print(df)