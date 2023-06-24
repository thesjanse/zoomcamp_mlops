import argparse
import pickle
import pandas as pd


parser = argparse.ArgumentParser(
        description="Predict trip duration for NYC taxi dataset."
    )
parser.add_argument("year")
parser.add_argument("month")
args = parser.parse_args()


CAT_FEATURES = ["PULocationID", "DOLocationID"]


def read_data(filename):
    df = pd.read_parquet(filename)

    df["ride_id"] = F"{args.year}/{args.month}_" + df.index.astype("str")
    df["duration"] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df["duration"] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[CAT_FEATURES] = df[CAT_FEATURES].fillna(-1).astype("int").astype("str")
    return df


if __name__ == "__main__":
    output_file = F"./auxiliary/yellow_tripdata_{args.year}-{args.month}.parquet"

    with open("./auxiliary/model.bin", "rb") as f_in:
        dv, model = pickle.load(f_in)

    df = read_data(F"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{args.year}-{args.month}.parquet")

    dicts = df[CAT_FEATURES].to_dict(orient="records")
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)
    df_result = pd.DataFrame(
        {
            "ride_id": df["ride_id"],
            "duration": y_pred
        }
    )
    df_result.to_parquet(
        output_file,
        engine="pyarrow",
        compression=None,
        index=False
    )
