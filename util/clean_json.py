import json

input_file = "input_file.json"
output_file = "output_file.json"

with open(input_file, "r") as infile:
    data = json.load(infile)

cleaned_data = []
for item in data:
    cleaned_item = {
        'First Name': item.get('First name', ''),
        'Last Name': item.get('Last name', ''),
        'Email': item.get('Email address', ''),
    }
    cleaned_data.append(cleaned_item)

with open(output_file, "w") as outfile:
    json.dump(cleaned_data, outfile, indent=4)

print(f"Cleaned data saved to {output_file}")
