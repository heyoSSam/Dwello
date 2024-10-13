import pandas as pd
import json

# Load the dataset
file_path = './dataset.xlsx'
data = pd.read_excel(file_path)

output_data = []
for index, row in data.iterrows():
    input_prompt = (f"Given that the population in {row['Republic of Kazakhstan']} is {row['Population']}, migration balance is {row['Migration balance']}, GDP is {row['GDP in KZT']}, number of transactions is {row['Number of purchase and sale transactions']}, Commissioning of individual and multi-apartment residential buildings is {row['Commissioning of individual and multi-apartment residential buildings']}, average salary is {row['Average Salary in KZT']}, price per square metr of new houses is {row['Price per square meter of new housing in KZT']}, price per square metr for resold houses is {row['Price per Square Meter of Resold Housing in KZT']} and inflation is {row['Inflation in %']} for {row['Year']}. Predict commissioning of individual and multi-apartment residential buildings in 2025, 2026 and 2027")

    output_prompt = f"The predicted commissioning of residential buildings is X for 2025, X for 2026 and X for 2027 units in {row['Republic of Kazakhstan']}."
    output_data.append({"input": input_prompt, "output": output_prompt})

# Save to JSON
with open('predictions.json', 'w') as json_file:
    json.dump(output_data, json_file, indent=4)

print("Prompts and predictions have been saved to predictions.json.")
