
##Project Overview

This project addresses the problem of short-term traffic speed forecasting using historical traffic sensor data.
Given a sequence of past traffic speed measurements from fixed road sensors, the goal is to predict the traffic speed at the next time interval.


##Problem Definition

    Task: Predict future traffic speed

    Type: Supervised learning (regression)

    Domain: Time-series forecasting

    Prediction horizon: Next time step (e.g., 5 minutes ahead)

    Inputs: Historical traffic speed readings

    Output: Traffic speed at the next time interval

Dataset

    The project uses the METR-LA traffic dataset, which contains:

        Traffic speed measurements

        Collected from multiple fixed highway sensors

        Recorded at regular 5-minute intervals

        Covering various traffic conditions (free-flow, congestion, rush hours)

    The dataset provides real sensor-based measurements, enabling supervised learning with ground-truth future values.    

Project Structure

    The project is implemented primarily in a single Jupyter notebook, organized into clearly defined sections:

        Problem Definition

        Dataset Understanding

        Data Preparation

        Feature Engineering

        Modeling

        Evaluation

        Discussion and Future Work    

Step 1: Problem Definition (before touching data)
Step 2: Data Understanding
Step 3: Data Preparation (critical)
Step 4: Feature Engineering (core intelligence)
Step 5: Modeling (very simple on purpose)
Step 6: Evaluation
Step 7: Iteration & Insights


## 1. Problem Definition
## 2. Dataset Overview
## 3. Sensor Selection
## 4. Data Preprocessing
## 5. Supervised Dataset Construction
## 6. Baseline Model
## 7. Linear Regression Model
## 8. Evaluation
## 9. Discussion & Insights