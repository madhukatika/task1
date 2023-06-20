import json

# List of JSON file paths to merge
file_paths = ['f1.json', 'f2.json', 'f3.json', 'f4.json', 'f5.json', 'f6.json', 'f7.json', 'f8.json', 'f9.json', 'f10.json', 'f11.json', 'f12.json', 'f13.json', 'f14.json', 'f15.json', 'f16.json', 'f17.json', 'f18.json']

merged_data = []

# Iterate through each file
for file_path in file_paths:
    with open(file_path, 'r') as file:
        data = json.load(file)
        merged_data.extend(data)

# Write the merged data to a new file
with open('merged_file.json', 'w') as merged_file:
    json.dump(merged_data, merged_file, indent=2)

print("JSON files merged successfully!")
