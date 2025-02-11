import pandas as pd

from src.utils.config import load_config
from src.utils.store import AssignmentStore


def main():
    store = AssignmentStore()
    config = load_config()

    dataset  = store.get_raw("car_price_dataset.csv")
    dataset = clean_booking_df(dataset)

    print(dataset.head(6))

    store.put_processed("dataset.csv", dataset)


def clean_booking_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    
def create_features(df: pd.DataFrame) -> pd.DataFrame:
    features = df.iloc[:,:9]



def create_target(df: pd.DataFrame, target_col: str) -> pd.DataFrame:
    target = df["Price"]

if __name__ == "__main__":
    main()
