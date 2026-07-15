def model_forecast(horizon=52):
    import random
    import pandas as pd
    forecast = [random.randint(0, 10) for _ in range(horizon)]

    return pd.DataFrame(forecast, index=range(horizon), columns=['forecast'])
