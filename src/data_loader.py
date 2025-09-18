import pandas as pd

def load_superstore_data(filepath):
    """
    Load Superstore dataset from CSV file.
    """
    return pd.read_csv(filepath)

# Contoh penggunaan:
# df = load_superstore_data('../data/SampleSuperstore.csv')
