from data.generator import generate_time_series, inject_anomalies
from features.rolling_stats import rolling_mean, rolling_std, z_score
from visualization.plot import plot_series
from features.rolling_stats import detect_anomalies

WINDOW = 20

data = generate_time_series()
data, true_anomalies = inject_anomalies(data)

means = rolling_mean(data, WINDOW)
stds = rolling_std(data, WINDOW)

z_scores = z_score(data, means, stds)

predicted_anomalies = detect_anomalies(z_scores)

print("True anomalies:", true_anomalies)
print("Predicted anomalies:", predicted_anomalies)

plot_series(data, true_anomalies, predicted_anomalies)