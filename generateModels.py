import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

file_path = "./dataset/temperatures.csv"
data = pd.read_csv(file_path)

years = [str(year) for year in range(1961, 2024)]
null_counts = data[years].isnull().sum(axis=1)
rows_to_remove = data[null_counts >= 35]
data.drop(rows_to_remove.index, inplace=True)


def preprocess(data, window=10):
    year_columns = [str(year) for year in range(1961, 2024)]
    data = data[["ISO2"] + year_columns]
    data = data.dropna(subset=["ISO2"]).reset_index(drop=True)

    melted_data = data.melt(
        id_vars=["ISO2"], var_name="Year", value_name="TemperatureChange"
    )
    melted_data["Year"] = melted_data["Year"].astype(int)
    melted_data = melted_data.dropna(subset=["TemperatureChange"])

    smoothed_data = (
        melted_data.groupby("ISO2")
        .apply(
            lambda group: group.assign(
                TemperatureChange=group["TemperatureChange"]
                .rolling(window=window, min_periods=1)
                .mean()
            )
        )
        .reset_index(drop=True)
    )

    return smoothed_data


data_cleaned = preprocess(data)


def train_and_export_models(data, output_dir="./models"):
    import os

    os.makedirs(output_dir, exist_ok=True)

    countries = data["ISO2"].unique()
    for country in countries:
        country_data = data[data["ISO2"] == country]
        X = country_data["Year"].values.reshape(-1, 1)
        y = country_data["TemperatureChange"].values

        model = LinearRegression()
        model.fit(X, y)

        model_path = os.path.join(output_dir, f"{country}.pkl")
        with open(model_path, "wb") as file:
            pickle.dump(model, file)


train_and_export_models(data_cleaned)
