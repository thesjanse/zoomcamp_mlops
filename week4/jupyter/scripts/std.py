import argparse
import pickle
import pandas as pd


CAT_FEATURES = ["PULocationID", "DOLocationID"]


def read_data(filename):
    df = pd.read_parquet(filename)
    
    df["duration"] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df["duration"] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[CAT_FEATURES] = df[CAT_FEATURES].fillna(-1).astype("int").astype("str")
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Predict trip duration for NYC taxi dataset."
    )

    parser.add_argument("year")
    parser.add_argument("month")

    args = parser.parse_args()

    with open("./auxiliary/model.bin", "rb") as f_in:
        dv, model = pickle.load(f_in)

    df = read_data(F"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{args.year}-{args.month}.parquet")

    dicts = df[CAT_FEATURES].to_dict(orient="records")
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)
    print(y_pred.std())
