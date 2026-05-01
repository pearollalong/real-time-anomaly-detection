"""
Synthetic time-series generator used for anomaly-detection experiments.

Discussion summary (for future reference):
- This module creates a discrete-time series, where one sample corresponds to
  one time step t in [0, n_points-1].
- Baseline signal is:
      data(t) = trend(t) + seasonality(t) + noise(t)
  where:
    - trend(t) = 0.05 * t
      A linear upward drift (diagonal centerline over time).
    - seasonality(t) = 10 * sin(2*pi*t/50)
      A sinusoidal component with:
        * amplitude = 10
        * period = 50 samples/cycle
        * frequency = 1/50 = 0.02 cycles/sample
      "Cycles/sample" means how much of a full wave is completed per data
      point. Here, each sample advances the wave by 2% of a full cycle.
      Therefore, every 50 samples completes one full seasonal cycle.
    - noise(t) ~ Normal(0, 1)
      Random Gaussian variation centered at zero (mean 0, std dev 1), used to
      mimic natural fluctuations/measurement noise.
- Combined interpretation: a sine wave whose centerline moves upward over time.
  Over one full cycle (50 samples), trend increases by 0.05*50 = 2.5.

Anomaly injection:
- inject_anomalies(...) selects random indices and adds either +20 or -20 to
  create sharp spike/drop point anomalies.
- It returns (modified_data, anomaly_indices) and leaves the original input
  unchanged by operating on a copy.
"""

import numpy as np

def generate_time_series(n_points=500):
    t = np.arange(n_points)

    # base signal
    trend = 0.05 * t
    seasonality = 10 * np.sin(2 * np.pi * t / 50)
    noise = np.random.normal(0, 1, n_points)

    data = trend + seasonality + noise

    return data

def inject_anomalies(data, n_anomalies=10):
    data = data.copy()
    indices = np.random.choice(len(data), n_anomalies, replace=False)

    for idx in indices:
        data[idx] += np.random.choice([20, -20])  # spike/drop

    return data, indices