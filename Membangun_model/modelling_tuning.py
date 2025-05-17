import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import f1_score
import lightgbm as lgb
import optuna

# Load Data
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'cryptonews_preprocessing', 'preprocessed_cryptonews.csv')

df = pd.read_csv(file_path)

# Prepare Features and Target
X_text = df['text_clean']
y = df['sentiment_encoded']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=2000)
X = vectorizer.fit_transform(X_text)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Define Objective Function for Optuna
def objective(trial):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 300),
        'learning_rate': trial.suggest_float('learning_rate', 0.005, 0.3),
        'max_depth': trial.suggest_int('max_depth', 3, 12),
        'num_leaves': trial.suggest_int('num_leaves', 10, 150),
        'min_child_samples': trial.suggest_int('min_child_samples', 5, 100),
        'subsample': trial.suggest_float('subsample', 0.6, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.6, 1.0),
        'random_state': 42,
        'verbose': -1
    }

    model = lgb.LGBMClassifier(**params)
    
    # Cross-validation
    scores = cross_val_score(model, X_train, y_train, cv=3, scoring='f1_weighted', n_jobs=-1)
    return np.mean(scores)

# Run Bayesian Optimization
print("[INFO] Starting Optuna optimization...")

study = optuna.create_study(direction='maximize')  # Maximize F1 score
study.optimize(objective, n_trials=50)  # Run 50 trials

# Print Best Results
print("\n[RESULTS] Best Parameters:")
print(study.best_params)

print(f"\n[RESULTS] Best Weighted F1 Score: {study.best_value:.4f}")

# Retrain with Best Params on Full Train Set
best_params = study.best_params
best_model = lgb.LGBMClassifier(**best_params, random_state=42)
best_model.fit(X_train, y_train)

# Evaluate on Test Set
y_pred = best_model.predict(X_test)
test_f1 = f1_score(y_test, y_pred, average='weighted')
print(f"\n[Test] Weighted F1 Score on Test Set: {test_f1:.4f}")

# Save the best model
best_model.booster_.save_model('best_lgbm_model.txt')
print("\n[INFO] Best model saved as 'best_lgbm_model.txt'")