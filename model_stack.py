def forecaster(forecast_horizon=52):
    import random

    forecast = [random.randint(0, 100) for _ in range(forecast_horizon)]
    return forecast

