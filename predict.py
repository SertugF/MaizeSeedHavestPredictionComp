from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from keras.optimizers import Adam
import keras
from matplotlib import pyplot
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def main():
    # load dataset
    data = pd.read_csv(
        os.path.join(
            "Data",
            "Training_Data",
            "1_Training_Trait_Data_2014_2021_NoMissingYield_Numeralized.csv",
        )
    )

    X = data.drop(["Yield_Mg_ha"], axis=1).values
    y = data["Yield_Mg_ha"].values

    X_Train, X_Val, y_Train, y_Val = train_test_split(
        X, y, test_size=0.20, random_state=0
    )

    # create model
    model = Sequential()
    model.add(Dense(128, input_dim=25, activation="relu"))  # input dimension is 25. !!!

    model.add(Dense(64, activation="relu"))

    model.add(Dense(32, activation="relu"))

    model.add(Dense(8, activation="relu"))

    model.add(Dense(1, activation="linear"))

    # compile model
    model.compile(
        loss="mean_squared_error",
        optimizer=Adam(lr=1e-3, decay=1e-3 / 200),
        metrics=["mse"],
    )

    # early stopping
    es = EarlyStopping(monitor="val_loss", mode="min", verbose=1, patience=10)

    # fit model
    history = model.fit(
        X_Train,
        y_Train,
        validation_data=(X_Val, y_Val),
        epochs=10,
        batch_size=32,
        callbacks=[es],
    )

    # predictions for validation set
    Pred_y_test = model.predict(X_Train)
    Pred_y_vall = model.predict(X_Val)

    # save predictions
    np.savetxt("train_results.csv", Pred_y_test, delimiter=",")
    np.savetxt("val_results.csv", Pred_y_vall, delimiter=",")

    # plot loss
    pyplot.plot(history.history["loss"], label="train")
    pyplot.plot(history.history["val_loss"], label="test")
    pyplot.legend()
    pyplot.show()

    # plot actual vs predicted
    plt.scatter(y_Train, Pred_y_test, color="red")
    plt.scatter(y_Val, Pred_y_vall, color="blue")
    plt.title("Actual vs Predicted")
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.show()

    # Compute r2 score
    print("R2 score for train set: ", r2_score(y_Train, Pred_y_test))

    print("R2 score for validation set: ", r2_score(y_Val, Pred_y_vall))

    # save model
    model.save("model.h5")


if __name__ == "__main__":
    main()
