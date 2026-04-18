from config_loader import load_config
import pandas as pd
import os



# function to load data
def load_data():

    config = load_config("../config/config.yaml")
    path = config["data"]["path"]

    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found")
    
    df = pd.read_csv(path)

    if df.empty:
        raise ValueError("DataFrame is empty")
    
    return df



