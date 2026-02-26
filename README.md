# Traffic Speed Prediction using METR-LA Dataset

## **Project Overview**
This project predicts the **next 5-minute traffic speed** for a selected sensor using historical traffic data from the **METR-LA dataset**.

- **Goal:** Forecast future traffic speed at a single sensor.  
- **Problem Type:** Time series regression (supervised learning).  
- **Dataset:** Traffic speed measurements from Los Angeles highways.

---

## **Data Preparation**
- Selected one sensor (`717447`) for simplicity.  
- Renamed the column to `Speed`.  
- Chronologically split the dataset to respect temporal order:  
  - **Train:** 70%  
  - **Validation:** 15%  
  - **Test:** 15%  

### Feature Engineering
1. **Lag Features:** Past 6 traffic speeds (`t-6` → `t-1`)  
2. **Delta Feature:** Change from previous speed  
   ```python
   delta_1[t] = Speed[t] - Speed[t-1]
   ```
   Used **delta[i-1]** to predict speed[i] to avoid data leakage.  

- **Final Feature Vector:** `[lag1, lag2, lag3, lag4, lag5, lag6, delta_1]` → 7 features  
- **Scaling:** Applied feature scaling to normalize input features.

---

## **Modeling**
- **Algorithm:** Linear regression trained using **Gradient Descent** (`SGDRegressor` from scikit-learn)

```python
from sklearn.linear_model import SGDRegressor

sgdr = SGDRegressor(max_iter=1000)
sgdr.fit(X_fe_norm, y_fe_train)

print(sgdr)
print(f"Number of iterations completed: {sgdr.n_iter_}, number of weight updates: {sgdr.t_}")
```

- **Baseline:** Only lag features  
- **Updated Model:** Lag features + delta

---

## **Results**

### **1 Baseline (lags only)**
- **Model Parameters:**  
  ```
  w: [ 0.5106 -0.0310 0.6673 0.6783 1.3630 11.0663 ]
  b: [50.0551]
  ```
- **Evaluation Set:**  
  ```
  Predictions: [41.80, 35.31, 35.94, 39.00]
  Targets:     [28.25, 31.13, 36.75, 35.25]
  MAE: 3.447
  R²: 0.851
  ```
- **Test Set:**  
  ```
  Predictions: [61.11, 61.13, 62.37, 63.74]
  Targets:     [61.50, 63.22, 65.63, 63.11]
  MAE: 4.149
  R²: 0.856
  ```

### **2 Updated Model (lags + delta)**
- **Model Parameters:**  
  ```
  w: [0.6148, 0.0943, 0.8416, 0.6295, 5.6938, 6.4994, 2.0225]
  b: [50.0500]
  ```
- **Evaluation Set:**  
  ```
  Predictions: [35.26, 36.45, 39.43, 38.12]
  Targets:     [31.13, 36.75, 35.25, 42.75]
  MAE: 3.442
  R²: 0.851
  ```
- **Test Set:**  
  ```
  Predictions: [60.94, 61.29, 62.67, 64.05]
  Targets:     [58.13, 61.11, 60.00, 62.25]
  MAE: 4.172
  R²: 0.857
  ```

**Observation:**  
Adding the **delta feature** slightly improves test performance while keeping evaluation performance similar. The model effectively captures short-term trends.

---

## 👤 Author

**Ahmed Mohamed**  
📧 [ahmed.mohamed04@hotmail.com](mailto:ahmed.mohamed04@hotmail.com)  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/ahmed04/)


