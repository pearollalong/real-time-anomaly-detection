import math

def rolling_std(data, window):
    stds = []

    for i in range(len(data)):
        if i < window:
            stds.append(None)
        else:
            window_data = data[i-window:i]
            mean = sum(window_data) / window
            variance = sum((x - mean) ** 2 for x in window_data) / window
            stds.append(math.sqrt(variance))

    return stds

def rolling_mean(data, window):
    means = []

    for i in range(len(data)):
        if i < window:
            means.append(None)
        else:
            window_data = data[i-window:i]
            means.append(sum(window_data) / window)

    return means

def z_score(data, means, stds):
    z_scores = []

    for i in range(len(data)):
        if means[i] is None or stds[i] is None or stds[i] == 0:
            z_scores.append(None)
        else:
            z = (data[i] - means[i]) / stds[i]
            z_scores.append(z)

    return z_scores

def detect_anomalies(z_scores, threshold=3):
    anomalies = []

    for i, z in enumerate(z_scores):
        if z is not None and abs(z) > threshold:
            anomalies.append(i)

    return anomalies