# sklearn genetic optic for featreu reduction
import matplotlib.pyplot as plt
from sklearn_genetic import GAFeatureSelectionCV
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.svm import SVC, SVR
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
import os


# data = pd.read_csv(
#     "E:\MaizeStuffTempDelete\MergedTrainingTrait_Meta_Soil_Weather_YieldLastNew.csv"
# )

data = pd.read_csv(
    os.path.join(
        "Data",
        "Training_Data",
        "1_Training_Trait_Data_2014_2021_NoMissingYield_Numeralized.csv",
    )
)
# check if there is any missing value and print
print(data.isnull().sum())

# check data info
print(data.info())

# Yield_Mg_ha is
X = data.drop(["Yield_Mg_ha"], axis=1).values
y = data["Yield_Mg_ha"].values


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=0
)

clf = SVR(kernel="poly", C=100, gamma="auto")

evolved_estimator = GAFeatureSelectionCV(
    estimator=clf,
    cv=3,
    scoring="accuracy",
    population_size=30,
    generations=20,
    n_jobs=-1,
    verbose=True,
    keep_top_k=2,
    elitism=True,
    error_score="raise",
)

# Train and select the features #all 3 fits are failed
evolved_estimator.fit(X_train, y_train)

# ValueError:
# All the 3 fits failed.
# It is very likely that your model is misconfigured.
# You can try to debug the error by setting error_score='raise'.

# Features selected by the algorithm
features = evolved_estimator.best_features_
print(features)

# Predict only with the subset of selected features
y_predict_ga = evolved_estimator.predict(X_test[:, features])
print(accuracy_score(y_test, y_predict_ga))
