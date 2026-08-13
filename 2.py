import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Generate historical network traffic data
np.random.seed(42)

dates = pd.date_range(start="2024-01-01", periods=120, freq="D")

trend = np.linspace(1000, 1600, 120)
noise = np.random.normal(0, 80, 120)

traffic = trend + noise

# Add abnormal traffic spikes representing possible DDoS activity
traffic[85:90] += 1200

data = pd.DataFrame({
    "Date": dates,
    "Network_Traffic": traffic
})

data.set_index("Date", inplace=True)

# Build ARIMA model
model = ARIMA(data["Network_Traffic"], order=(2, 1, 2))
model_fit = model.fit()

# Forecast future traffic
forecast = model_fit.forecast(steps=15)

# Plot historical and forecasted traffic
plt.figure(figsize=(10, 5))

plt.plot(
    data.index,
    data["Network_Traffic"],
    label="Historical Traffic"
)

future_dates = pd.date_range(
    start=data.index[-1] + pd.Timedelta(days=1),
    periods=15,
    freq="D"
)

plt.plot(
    future_dates,
    forecast,
    label="Forecasted Traffic"
)

plt.title("ARIMA Forecasting of Network Traffic")
plt.xlabel("Date")
plt.ylabel("Network Traffic")
plt.legend()
plt.grid()
plt.show()

print("Forecasted Network Traffic:")
print(forecast)