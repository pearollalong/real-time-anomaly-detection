from data.generator import generate_time_series, inject_anomalies
import matplotlib.pyplot as plt

data = generate_time_series()
data_with_anomaly, anomaly_indices = inject_anomalies(data)

for idx in anomaly_indices:
    print(f"Anomaly at index {idx}: {data_with_anomaly[idx]}")
    print(f"Original value: {data[idx]}")
    print("--------------------------------")

plt.plot(data, label="Original")
plt.plot(data_with_anomaly, label="With Anomaly")
plt.legend()
plt.show()