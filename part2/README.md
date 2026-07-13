# Part 2 – Supervised Machine Learning

## Objective

Train a supervised machine learning model to predict California house prices.

## Model

Random Forest Regressor

## Workflow

1. Load dataset
2. Create categorical feature
3. Handle missing values
4. Encode categorical variables
5. Split into training and testing sets
6. Train Random Forest model
7. Evaluate model
8. Save trained model

## Evaluation Metrics

- MAE
- MSE
- RMSE
- R² Score

## How to Run

```bash
pip install -r requirements.txt
python train_model.py
```

## Output

A trained model is saved in:

```
models/house_price_model.pkl
```

## Conclusion

The Random Forest Regressor performs well because it captures nonlinear relationships between housing features and house prices. The saved model can be reused for predictions without retraining.
