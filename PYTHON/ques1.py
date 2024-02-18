import json

file_path = r'C:\Users\hotst\OneDrive\Desktop\vscode\WNS Case Study\PYTHON\data.txt'

with open(file_path, 'r') as file:
    data = json.load(file)

for person in data['people']:
    print("Name:", person['name'])
    print("Address:", person['address'])
    print("Mobile Numbers:", ", ".join(person['mobile_numbers']))
    print("Date of Birth:", person['date_of_birth'])
    print("\n")
import json
import pandas as pd

# Specify the path to your JSON file
file_path = r'C:\Users\hotst\OneDrive\Desktop\vscode\WNS Case Study\PYTHON\data.txt'

# Read data from the file
with open(file_path, 'r') as file:
    data = json.load(file)

# Create an empty DataFrame to store the data
df = pd.DataFrame(data['people'])

# Print the DataFrame or perform further operations
print(df)
