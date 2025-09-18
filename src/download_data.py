import os
import shutil
import kagglehub

def download_superstore_dataset(target_dir):
    os.makedirs(target_dir, exist_ok=True)
    
    # Download dataset using kagglehub
    path = kagglehub.dataset_download("vivek468/superstore-dataset-final")
    print("Path to dataset files:", path)
    
    # Copy files to our data directory
    for file in os.listdir(path):
        if file.endswith('.csv'):
            shutil.copy(os.path.join(path, file), os.path.join(target_dir, file))
            print(f"Copied {file} to {target_dir}")
    
    print('Download dan copy selesai!')

if __name__ == "__main__":
    download_superstore_dataset("../data")
