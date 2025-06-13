import json

input_file = "input_file.json"
output_file = "output_file.json"

with open(input_file, "r") as infile:
    data = json.load(infile)

cleaned_data = []
for item in data:
    first = item.get('First name', '').strip()
    last = item.get('Last name', '').strip()
    full_name = f"{first} {last}".strip()

    cleaned_item = {
        'Name': full_name,
        'Email': item.get('Email', ''),
    }
    cleaned_data.append(cleaned_item)

with open(output_file, "w") as outfile:
    json.dump(cleaned_data, outfile, indent=4)

print(f"Cleaned data saved to {output_file}")
