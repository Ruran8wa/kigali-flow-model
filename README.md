# KigaliFlow: Traffic Congestion Classification in Kigali

## Problem Statement

Current traffic apps don’t reflect local realities in Kigali, such as weather patterns, road types, or community events. Our goal is to use machine learning to classify traffic congestion levels — Low, Moderate, or High — based on simulated real-world conditions like time of day, road type, event presence, and weather.

## Dataset

A simulated dataset was generated with 1000 samples using features such as:
- `time_of_day` (morning, afternoon, evening)
- `weather` (clear, rain, foggy, cloudy)
- `road_type` (main road, secondary road, residential)
- `event` (0 = no event, 1 = event nearby)
- `congestion_level` (target: Low, Moderate, High)

## Model Summary Table

| Instance | Optimizer | Regularizer         | Epochs | Early Stopping | Layers         | LR      | Accuracy | F1 Score | Recall | Precision |
|----------|-----------|---------------------|--------|----------------|----------------|---------|----------|----------|--------|-----------|
| 1 (ML)   | —         | —                   | —      | —              | —              | —       | 0.740    | 0.743    | 0.740  | 0.748     |
| 2 (NN)   | Adam      | None                | 30     | No             | 64 → 32 → 3    | —       | 0.847    | 0.844    | 0.847  | 0.850     |
| 3 (NN)   | RMSprop   | L1 (0.001)          | 50     | Yes            | 64 → 32 → 3    | 0.001   | 0.873    | 0.874    | 0.873  | 0.875     |
| 4 (NN)   | Adam      | L2 (0.001)          | 60     | Yes            | 128 → 64 → 3   | 0.0005  | 0.860    | 0.860    | 0.860  | 0.863     |
| 5 (NN)   | Nadam     | L1 + L2 (0.001 each)| 60     | Yes            | 256 → 128 → 3  | 0.0007  | 0.813    | 0.815    | 0.813  | 0.824     |

## Observations & Summary

### Best Performing Model
- Model 3 (Neural Network with RMSprop + L1 + Dropout + Early Stopping)
- Achieved the highest F1 Score (0.874) and Accuracy (0.873)
- Balanced generalization and performance well

### Weakest Performing Model
- Model 5 (Nadam with L1+L2 + Dropout 0.5)
- Possibly over-regularized, leading to lower recall on the Moderate class

### Classic ML vs Neural Network
- Model 1 (Logistic Regression) performed decently with Accuracy: 0.74, but Neural Networks clearly outperformed it on all key metrics, especially F1 and Recall.

## Key Takeaways
- Dropout and regularization improve generalization.
- RMSprop provided stable, consistent training on this task.
- Early stopping prevented overfitting in deeper models.
- Neural Networks significantly outperform classical ML when tuned correctly.

## Saved Models

All trained models are stored in the `saved_models/` folder:
- `model-1.pkl`
- `model-2.keras`
- `model-3.keras`
- `model-4.keras`
- `model-5.keras`


## Link to the submission video

- `https://youtu.be/s88a2FEeMGA`
