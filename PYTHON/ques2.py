import os
import pandas as pd
from datetime import datetime

Path = r'C:\Users\hotst\OneDrive\Desktop\vscode\WNS Case Study\PYTHON\samp.xlsx'

targetPath = r'C:\Users\hotst\OneDrive\Desktop\vscode\WNS Case Study\PYTHON\bundle.xlsx'

def read_csv_and_store(file_path, tracking_file):
    df = pd.read_csv(file_path)

    print(df.head())

    with open(tracking_file, 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{file_path},{timestamp}\n")

def process_files(directory, tracking_file):
    csv_files = [file for file in os.listdir(directory) if file.startswith("Sales_Data") and file.endswith(".csv")]

    processed_files = set()
    if os.path.exists(tracking_file):
        with open(tracking_file, 'r') as file:
            for line in file:
                filename, timestamp = line.strip().split(',')
                processed_files.add(filename)

    for file in csv_files:
        if file not in processed_files:
            file_path = os.path.join(directory, file)
            read_csv_and_store(file_path, tracking_file)

process_files(Path, targetPath)
