import matplotlib.pyplot as plt

def plot_series(data, real_anomalies, predicted_anomalies):
    plt.figure(figsize=(12, 6))
    
    plt.plot(data, label="Time Series")
    
    # mark anomalies
    plt.scatter(real_anomalies, [data[i] for i in real_anomalies], color='green', label="Real Anomalies")
    plt.scatter(predicted_anomalies, [data[i] for i in predicted_anomalies], color='red', label="Predicted Anomalies")
    
    plt.legend()
    plt.title("Anomaly Detection (Z-score)")
    plt.show()