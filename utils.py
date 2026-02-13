import matplotlib.pyplot as plt
import numpy as np

def plot_features_vs_label(X, y, feature_names=None, sample_size=500):
    """
    Plots each feature against the label using a random subset of the data.

    Parameters:
        X : np.array, shape (n_samples, n_features)
            Features
        y : np.array, shape (n_samples,)
            Labels
        feature_names : list of strings, optional
            Names of the features for titles
        sample_size : int
            Number of samples to plot (random subset)
    """
    n_samples, n_features = X.shape
    
    # Randomly sample indices if dataset is large
    if sample_size < n_samples:
        idx = np.random.choice(n_samples, size=sample_size, replace=False)
        X_plot = X[idx]
        y_plot = y[idx]
    else:
        X_plot = X
        y_plot = y

    # Plot each feature
    for i in range(n_features):
        plt.figure(figsize=(6,4))
        plt.scatter(X_plot[:, i], y_plot, alpha=0.5)
        title = feature_names[i] if feature_names else f"Feature {i+1} vs Label"
        plt.title(title)
        plt.xlabel("Feature value")
        plt.ylabel("Label (Next Speed)")
        plt.show()
