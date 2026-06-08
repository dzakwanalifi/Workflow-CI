import sys
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

data_path = sys.argv[1] if len(sys.argv) > 1 else "mamikos_preprocessing_dataset.csv"
df = pd.read_csv(data_path)

feature_cols = [col for col in df.columns if col != 'clean_discount_price']
X = df[feature_cols]
y = df['clean_discount_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

mlflow.sklearn.autolog()

with mlflow.start_run(run_name="RandomForest_CI_Retrain"):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"CI Retrain Random Forest -> MSE: {mse:.4f}, R2: {r2:.4f}")
